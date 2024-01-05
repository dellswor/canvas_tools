create table academic_cal (
    block_pk    serial primary key, -- DB identifier for the block
    block       char(1),            -- The block in question
    year        integer,            -- The year
    academic_yr char(9),            -- Academic year the block is in
    start_dt    date,               -- First day of class
    end_dt      date
);
insert into dbfeatures (name,version,installed) VALUES ('academic_cal',0,now())

insert into academic_cal (block, year, academic_yr) VALUES ('1',2017,'2017-2018');
insert into academic_cal (block, year, academic_yr) VALUES ('2',2017,'2017-2018');
insert into academic_cal (block, year, academic_yr) VALUES ('3',2017,'2017-2018');
insert into academic_cal (block, year, academic_yr) VALUES ('4',2017,'2017-2018');
insert into academic_cal (block, year, academic_yr) VALUES ('J',2017,'2017-2018');
insert into academic_cal (block, year, academic_yr) VALUES ('5',2017,'2017-2018');
insert into academic_cal (block, year, academic_yr) VALUES ('6',2018,'2017-2018');
insert into academic_cal (block, year, academic_yr) VALUES ('7',2018,'2017-2018');
insert into academic_cal (block, year, academic_yr) VALUES ('8',2018,'2017-2018');
insert into academic_cal (block, year, academic_yr) VALUES ('A',2018,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('B',2018,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('C',2018,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('1',2018,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('2',2018,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('3',2018,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('4',2018,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('J',2018,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('5',2018,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('6',2019,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('7',2019,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('8',2019,'2018-2019');
insert into academic_cal (block, year, academic_yr) VALUES ('A',2019,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('B',2019,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('C',2019,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('1',2019,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('2',2019,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('3',2019,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('4',2019,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('J',2019,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('5',2019,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('6',2020,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('7',2020,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('8',2020,'2019-2020');
insert into academic_cal (block, year, academic_yr) VALUES ('A',2020,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('B',2020,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('C',2020,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('1',2020,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('2',2020,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('3',2020,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('4',2020,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('J',2020,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('5',2020,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('6',2021,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('7',2021,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('8',2021,'2020-2021');
insert into academic_cal (block, year, academic_yr) VALUES ('A',2021,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('B',2021,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('C',2021,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('1',2021,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('2',2021,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('3',2021,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('4',2021,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('J',2021,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('5',2021,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('6',2022,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('7',2022,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('8',2022,'2021-2022');
insert into academic_cal (block, year, academic_yr) VALUES ('A',2022,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('B',2022,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('C',2022,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('1',2022,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('2',2022,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('3',2022,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('4',2022,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('J',2022,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('5',2022,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('6',2023,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('7',2023,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('8',2023,'2022-2023');
insert into academic_cal (block, year, academic_yr) VALUES ('A',2023,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('B',2023,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('C',2023,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('1',2023,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('2',2023,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('3',2023,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('4',2023,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('J',2023,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('5',2023,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('6',2024,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('7',2024,'2023-2024');
insert into academic_cal (block, year, academic_yr) VALUES ('8',2024,'2023-2024');
