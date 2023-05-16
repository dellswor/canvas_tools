// The dbfeatures table provides compatibility information so that scripts
// can check that they will run correctly against the current database.
// Actions that change tables/views/stored procs/etc should add/delete
// rows from the dbfeatures table.
// Adding a column to a table is always safe, just add a new row with higher 
//        version number
// Removing a column from a table is not safe, delete existing rows and insert a
//        new row. Then identify which scripts break and fix them.
create table dbfeatures (
    name        varchar(128), // feature name, must be unique
    version     integer,      // version number
    installed timestamp       // when the feature was added
);

// Cache for courses
create table allcourses (
    course_pk   serial primary key, // DB identifier for the course
    canvas_id   integer, // The id number for the course in the canvas API
    course_title    varchar(128), // human name for the course
    course_number   integer,      // Course number in the college catalog
    block           integer,      // Block of the course delivery
    ignore          boolean DEFAULT(FALSE) // Unused course, ignore in view
);
create view courses AS select * from allcourses where ignore=FALSE;
insert into dbfeatures (name,version,installed) VALUES ('courses_table',0,now());

// Cache for students
create table allstudents (
    student_pk  serial primary key, // DB identifier for the student
    canvas_id   integer,            // the id in the canvas API
    email       varchar(256),       // Student email address
    ccusername  varchar(128),       // Student username for SSO
    first_name  varchar(128),       // Student first name
    last_name   varchar(128),       // Student last name
    gender      varchar(128),       // Student preferred gender
    notes       text                // Arbitrary text to help with letters
);
create view students AS select * from allstudents;
insert into dbfeatures (name,version,installed) VALUES ('student_table',0,now())
