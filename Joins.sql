USE railwaydb;

SELECT * FROM user;
SELECT * FROM station;
SELECT * FROM train;
SELECT * FROM ticket_booking;
SELECT * FROM ticket_status;
SELECT * FROM payment;
SELECT * FROM schedule;
SELECT * FROM train_classes;
SELECT * FROM admin;
SELECT * FROM cancellations;



#INNER JOIN
SELECT 
    t.Train_no,
    t.Train_name,
    s1.Station_name AS SOURCE_STN,
    s2.Station_name AS DESTINATION_STN
FROM 
    Train t
JOIN 
    Station s1 ON t.Source_stationid = s1.Station_ID
JOIN 
    Station s2 ON t.Destination_stationid = s2.Station_ID
WHERE 
    s1.Location IN('Mysore', 'Banglore');


select t.train_no, s.station_id, s.arrival_time, s.departure_time, t.running_days
from train t
join station s
on t.source_stationid = s.station_id;

#SELF JOIN
select * from 
station t1
join station t2
on t1.IsSource_station=t2.IsDestination_station;

# MULTIPLE JOIN
SELECT 
    t.train_no, 
    t.train_name, 
    t.source_stationid AS source,
    s1.station_name AS source_station_name,
    t.destination_stationid AS destination,
    s2.station_name AS destination_station_name
FROM train t
JOIN station s1 ON t.source_stationid = s1.station_id
JOIN station s2 ON t.destination_stationid = s2.station_id
LIMIT 0, 1000;

#LEFT JOIN


Select distinct User_id, Train_no, source_stationid, destination_stationid
from user u
join station s
on u.city=s.Location
join train t 
on s.Station_ID =t.Source_stationid or s.Station_ID = t.Destination_stationid
order by u.User_ID;

Select distinct u.User_ID, s.Station_ID, s.Station_name, s.IsSource_station, s.IsDestination_station, t.train_no, t.Train_name,
t.train_type, t.Source_stationid, t.Destination_stationid, t.total_seats
from user u
join station s
on u.city=s.Location
join train t
on s.Station_ID =t.Source_stationid or s.Station_ID = t.Destination_stationid
order by user_id;


Select u.User_ID, u.name, s.Station_ID,s.IsSource_station, s.IsDestination_station, u.city,train_no, train_type, total_seats 
from user u
join station s on  u.city=s.Location
join train t on t.source_stationid=s.station_id
order by u.User_ID;


SELECT u.User_ID, u.name, s.Station_ID, s.IsSource_station, s.IsDestination_station, 
       u.city, t.train_no, t.train_type, t.total_seats
FROM user u
JOIN station s ON u.city = s.Location
JOIN train t ON t.source_stationid = s.station_id
UNION
SELECT NULL AS User_ID, NULL AS name, NULL AS Station_ID, NULL AS IsSource_station, 
       NULL AS IsDestination_station, NULL AS city, NULL AS train_no, 
       NULL AS train_type, NULL AS total_seats
FROM train_classes tc
ORDER BY User_ID;

#COMPOUND JOIN

select *
from ticket_Booking tb
join payment p
using(booking_id,user_id);

#NATURAL JOIN
select * 
from ticket_booking
natural join payment;

#CROSS JOIN
select * from 
user, ticket_booking;