create table course_student (
    course_fk       integer references allcourses(course_pk),  -- course
    student_fk      integer references allstudents(student_pk) -- student
);
insert into dbfeatures (name,version,installed) VALUES ('course_to_student_table',0,now());

