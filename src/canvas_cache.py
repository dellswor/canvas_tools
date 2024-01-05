# canvas_cache.py
#
# The Canvas datamodel, as exposed by the API, combine with API latencies makes
# direct use of the API painful for many questions. The caching layer exists
# to make a local copy of Canvas data for much faster access.
# 

import os
import re
from core import BadBlockString
from zoneinfo import ZoneInfo
import psycopg
from psycopg.rows import dict_row

from core import get_canvas_connection

if __name__=="__main__":
    print("The canvas_cache should not be run directly!",file=sys.stderr)
    exit(1)

_DATABASE_NAME = 'canvastools'
# By default, access to the cache uses the running user's name
_DATABASE_USER = os.getlogin()

def _initialize():
    pass

def get_courses_for_block(block_string):
    '''Returns a list of dicts representing courses for the given block_string
       If no courses are found, an empty list is returned
       keys: course_pk, canvas_id, title, number, block, year
    '''
    ret = list()
    bs_pat = re.compile(r'(\d{4})b(\w)')
    m = bs_pat.match(block_string)
    if m:
        qargs = dict()
        qargs['year'] = m.group(1)
        qargs['block'] = m.group(2)
        with psycopg.connect("dbname=%s user=%s"%(_DATABASE_NAME,_DATABASE_USER)) as dbconn:
            with dbconn.cursor(row_factory=dict_row) as cur:
                query = """SELECT course_pk as course_pk, canvas_id as canvas_id, course_title as title, course_number as number, ac.block as block, ac.year as year, ac.start_dt as start_dt, ac.end_dt as end_dt
                           FROM academic_cal ac
                           JOIN courses cs ON ac.block_pk=cs.block
                           WHERE ac.year=%(year)s and ac.block=%(block)s
                        """
                cur.execute(query,qargs)
                rset = cur.fetchall()
                for row in rset:
                    row['start_dt'] = row['start_dt'].replace(tzinfo=ZoneInfo('America/Denver'))
                    row['end_dt'] = row['end_dt'].replace(tzinfo=ZoneInfo('America/Denver'))
                    ret.append(row)
    else:
        raise BadBlockString(block_string)
    return ret
    
def cache_students_in_course(canvas_id):
    '''Caches the students enrolled in the course with id canvas_id
       Students not already in the DB are added. Existing associations are
       not duplicated.
    '''
    # Get the course
    conn = get_canvas_connection()
    course = conn.get_course(canvas_id)
    if course is None:
        raise UnknownCourse("canvas_id was not found in canvas..."%canvas_id)

    # Loop over the users and check the DB
    users = course.get_users(enrollment_type=['student'])
    with psycopg.connect("dbname=%s user=%s"%(_DATABASE_NAME,_DATABASE_USER)) as dbconn:
        with dbconn.cursor(row_factory=dict_row) as cur:
            cquery = """SELECT course_pk FROM allcourses WHERE canvas_id=%(canvas_id)s"""
            aquery = """SELECT course_fk,student_fk FROM course_student WHERE course_fk=%(course_pk)s AND student_fk=%(student_pk)s"""

            squery = """SELECT student_pk FROM allstudents WHERE canvas_id=%(student_id)s"""
            iquery = """INSERT INTO allstudents (canvas_id,email,ccusername,first_name,last_name) VALUES (%(canvas_id)s,%(email)s,%(ccusername)s,%(first_name)s,%(last_name)s) RETURNING student_pk as student_pk"""
            iaquery = """INSERT INTO course_student (course_fk,student_fk) VALUES (%(course_pk)s,%(student_pk)s)"""
            for user in users:
                qargs = dict()
                qargs['canvas_id'] = canvas_id
                qargs['student_id']= user.id
                qargs['email']     = user.email
                qargs['ccusername']= qargs['email'].split('@')[0]
                qargs['first_name']= user.sortable_name.split(', ')[1]
                qargs['last_name'] = user.sortable_name.split(', ')[0]
                # Get the student pk, add the student if they don't exist
                cur.execute(squery,qargs)
                r = cur.fetchone()
                if r is None:
                    cur.execute(iquery,qargs)
                    r = cur.fetchone()
                qargs['student_pk'] = r['student_pk']
                # Make the association if it doesn't exist
                cur.execute(cquery,qargs)
                r = cur.fetchone()
                if r is None:
                   raise UnknownCourse("canvas_id %s not found in cache"%canvas_id)
                qargs['course_pk'] = r['course_pk']
                cur.execute(aquery,qargs)
                r = cur.fetchone()
                if r is None:
                    # add the association
                    cur.execute(iaquery,qargs)

def sync_courses():
    code_pat = re.compile(r'^(\w+\d+) \d+ Block (\w)$')
    term_pat = re.compile(r'^\w+ (\d+)$')

    conn = get_canvas_connection()
    courses = conn.get_courses(include=['term'])
    with psycopg.connect("dbname=%s user=%s"%(_DATABASE_NAME,_DATABASE_USER)) as dbconn:
        with dbconn.cursor() as cur:
            for course in courses:
                d = dict()
                d['id'] = course.id
                d['name'] = course.name
                d['code'] = course.course_code
                try:
                    d['orig'] = course.original_name
                except AttributeError as e:
                    d['orig'] = course.name
                m = term_pat.match(course.term['name'])
                if m:
                    d['year'] = int(m.group(1))
                else:
                    d['year'] = 0
                m = code_pat.match(d['code'])
                if m:
                    d['course'] = m.group(1)
                    d['block']  = m.group(2)
                if 'block' in d and d['year']>2000:
                    cur.execute("SELECT block_pk FROM academic_cal WHERE block=%(block)s AND year=%(year)s",d)
                    r = cur.fetchone()
                    if r:
                        d['block_fk'] = r[0]
                    else:
                        d['block_fk'] = -1

                    cur.execute("SELECT course_pk FROM allcourses WHERE canvas_id=%(id)s",d);
                    r = cur.fetchone()
                    if r:
                        # existing course, do nothing
                        pass
                    else:
                        cur.execute("INSERT INTO allcourses (canvas_id,course_title,course_number,block) VALUES (%(id)s, %(name)s, %(course)s, %(block_fk)s)",d)
                        if d['name']==d['orig']:
                            cur.execute("SELECT course_title FROM course_titles WHERE course_num=%(course)s AND %(year)s BETWEEN start_yr AND end_yr",d);
                            r = cur.fetchone()
                            if r:
                                conn.set_course_nickname(d['id'], "%sb%s %s"%(d['year'],d['block'],r[0]))
                        # Add the students to the cache
                        cache_students_in_course(d['id'])    
                else:
                    cur.execute("INSERT INTO allcourses (canvas_id,course_title) VALUES (%(id)s, %(name)s)",d)
                    
_initialize()
