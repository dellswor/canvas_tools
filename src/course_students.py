#! /usr/bin/python3

import sys
import canvas_cache
from core import yesno,get_canvas_connection
from datetime import timedelta

if __name__=="__main__":
    # check the args
    if len(sys.argv)!=3 or sys.argv[1]=='-h' or sys.argv[2] not in ['cache_students']:
        print("Usage: python3 %s <YYYYbB> <action>")
        print("valid actions:")
        print("    cache_students - recache the students associated with the course")
        exit(1)

    # Find the class to operate on
    classes = canvas_cache.get_courses_for_block(sys.argv[1])
    if len(classes)==0:
        print("No classes found in the cache for block %s",sys.argv[1])
        exit(1)
    cl = None
    if len(classes)>1:
        print("Multiple classes found in the cache for block %s",sys.argv[1])
        while cl is None:
            print("Please select the course you would like to operate on:")
            for i in range(len(classes)):
                print("%d : %d %s %s"%(i,classes[i]['canvas_id'],classes[i]['number'],classes[i]['title']))
            try:
                i = int(input("list entry> "))
                if i<0 or i>=len(classes):
                    raise Exception()
                cl = classes[i]
            except:
                print("Entry must be the numeric index of the class in the list")
    else:
        cl = classes[0]

    # do the operation
    if sys.argv[2]=='cache_students':
        canvas_cache.cache_students_in_course(cl['canvas_id'])
