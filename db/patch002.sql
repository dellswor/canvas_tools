create table course_titles (
    course_title    varchar(128), -- long name of the course
    course_num      varchar(12),  -- course number
    start_yr        integer,      -- first year the title is active
    end_yr          integer       -- last year the title is active
);
insert into dbfeatures (name,version,installed) VALUES ('course_titles_table',0,now());

INSERT INTO course_titles (course_num,course_title,start_yr,end_yr) VALUES ('CP115','Computational Thinking',2016,9999);
INSERT INTO course_titles (course_num,course_title,start_yr,end_yr) VALUES ('CP274','Software Design',2016,9999);
INSERT INTO course_titles (course_num,course_title,start_yr,end_yr) VALUES ('CP122','Computer Science I',1980,9999);
INSERT INTO course_titles (course_num,course_title,start_yr,end_yr) VALUES ('CP222','Computer Science II',1980,9999);
INSERT INTO course_titles (course_num,course_title,start_yr,end_yr) VALUES ('CP341','Topics in Computer Science',1980,9999);
INSERT INTO course_titles (course_num,course_title,start_yr,end_yr) VALUES ('CP499','Team Software Project',2018,9999);
INSERT INTO course_titles (course_num,course_title,start_yr,end_yr) VALUES ('CP275','Computer Organization',1980,9999);
