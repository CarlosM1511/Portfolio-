

CREATE TABLE date_dim (
    full_date date,
    month int,
    day int,
    month_name varchar,
    day_name varchar,
    weekend	boolean,
    date_key int PRIMARY KEY

);
CREATE TABLE stations (
    id int PRIMARY KEY,
    station_name varchar,
    latitude float,
    longitude float
);
CREATE TABLE demo (
    user_type varchar,
    birth_year float,
    gender int,
    age	float,
    demo_id int PRIMARY KEY

);
CREATE TABLE weather (
    rec_date date,
    avg_wind float,
    prcp float,
    snow_amt float,
    snow_depth float,
    tavg int,
    tmax int,
    tmin int,
    rain boolean,
    snow boolean,
    date_key int PRIMARY KEY

);
CREATE TABLE rides (
    trip_duration int,
    start_time date,
    stop_time date,
    start_station_id int,
    end_station_id int,
    bike_id int,
    id int PRIMARY KEY,
    trip_minutes float,
    trip_hours float,
    date_key int,
    demo int

);