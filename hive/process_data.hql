create external table if not exists temp
(
    accident struct<address:string,postcode:int,victim_type:string,injury:string>,
    number int
)
row format delimited
fields terminated by '\t'
collection items terminated by ','
location '/project/output/';

create external table if not exists zipcodes
(
    postcode int,
    district string
)
row format delimited
fields terminated by ',';

load data
inpath '/project/zips-boroughs.csv'
into table zipcodes;

alter table zipcodes
set tblproperties
(
    "skip.header.line.count"="1"
);

create table if not exists temp2
(
    address string,
    postcode int,
    victim_type string,
    injury string,
    number int
);

insert into temp2
select
    accident.address,
    accident.postcode,
    accident.victim_type,
    accident.injury,
    number
from temp;

create table if not exists accidents
(
    address string,
    victim_type string,
    injury string,
    number int,
    postcode int,
    district string
);

insert into accidents
select
    t2.address,
    t2.victim_type,
    t2.injury,
    t2.number,
    z.postcode,
    z.district
from temp2 t2
join zipcodes z on t2.postcode = z.postcode;

create external table if not exists results_injured
(
    address string,
    victim_type string,
    injury string,
    sum int
)
row format delimited
fields terminated by '\t'
stored as textfile location '/project/hive/injured';

create table if not exists results_killed
(
    address string,
    victim_type string,
    injury string,
    sum int
)
row format delimited
fields terminated by '\t'
stored as textfile location '/project/hive/killed';

create view pedestrians_injured as
select address, victim_type, injury, sum(number) as sum
from accidents
where district = 'MANHATTAN' and victim_type = 'pedestrian' and injury = 'injured'
group by address, victim_type, injury
order by sum desc
limit 3;

create view pedestrians_killed as
select address, victim_type, injury, sum(number) as sum
from accidents
where district = 'MANHATTAN' and victim_type = 'pedestrian' and injury = 'killed'
group by address, victim_type, injury
order by sum desc
limit 3;

create view cyclists_injured as
select address, victim_type, injury, sum(number) as sum
from accidents
where district = 'MANHATTAN' and victim_type = 'cyclist' and injury = 'injured'
group by address, victim_type, injury
order by sum desc
limit 3;

create view cyclists_killed as
select address, victim_type, injury, sum(number) as sum
from accidents
where district = 'MANHATTAN' and victim_type = 'cyclist' and injury = 'killed'
group by address, victim_type, injury
order by sum desc
limit 3;

create view motorists_injured as
select address, victim_type, injury, sum(number) as sum
from accidents
where district = 'MANHATTAN' and victim_type = 'motorist' and injury = 'injured'
group by address, victim_type, injury
order by sum desc
limit 3;

create view motorists_killed as
select address, victim_type, injury, sum(number) as sum
from accidents
where district = 'MANHATTAN' and victim_type = 'motorist' and injury = 'killed'
group by address, victim_type, injury
order by sum desc
limit 3;

insert overwrite table results_injured
select * from pedestrians_injured
union all
select * from cyclists_injured
union all
select * from motorists_injured;

insert overwrite table results_killed
select * from pedestrians_killed
union all
select * from cyclists_killed
union all
select * from motorists_killed;
