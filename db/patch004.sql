create table academic_holidays (
    start_dt    date,
    end_dt      date,
    comment     text
);
insert into dbfeatures (name,version,installed) VALUES ('holidays_table',0,now());
