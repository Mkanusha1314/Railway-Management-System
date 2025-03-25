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

INSERT INTO user(name, age, gender, phone_no, city)
VALUES('Manoj', 32, 'M', 985678876, 'Hassan'),
('Shiva', 45, 'M', 851678766, 'Mandya'),
('Asha', 51, 'F', 951896766, 'Banglore'),
('Jagan', 23, 'M', 987576466, 'Kolar');

INSERT INTO ticket_booking (User_id, Train_no, source_stationid, destination_stationid,  seat_no, Class, Fare, Payment_status, Booking_status)
VALUES 
(2,16,3,13,44,'First_class',150, 'Completed', 'Confrimed' ),
(3,18,3,10,13,'Economy',100,'Completed', 'Confrimed' ),
(4,16,3,2,60,'Business',200,'Completed','Confrimed' ),
(5,15,1,12,22,'Economy',100,'Pending','Waiting' ),
(6,13,3,13,58,'Business',200,'Completed','Confrimed'),
(7,14,7,2,103,'First_class',150,'Pending','Waiting'),
(8,12,5,4,200,'Economy',100,'Pending','Waiting' ),
(9,17,5,2,108,'First_class',150,'Completed','Confrimed' ),
(10,19,3,8,72,'Business',200,'Completed','Confrimed');

Insert into ticket_status (Booking_id, Current_status)
select Booking_id, Booking_status
from ticket_Booking;

Insert into payment(booking_id, user_id, amount, payment_method, payment_status)
select booking_id, user_id, fare, 'Net-banking' as payment_method, payment_status
from ticket_booking;

Insert into schedule (train_no, station_id, arrival_time, departure_time, day_of_week)
select t.train_no, s.station_id, s.arrival_time, s.departure_time, t.running_days
from train t
join station s
on t.source_stationid = s.station_id;

INSERT INTO train_classes (train_no, class_name, fare_per_seat, seat_count)
SELECT train_no, 'Economy' AS class_name, 100 AS fare_per_seat, 200 AS seat_count
FROM train
UNION ALL
SELECT train_no, 'First-Class' AS class_name, 150 AS fare_per_seat, 250 AS seat_count
FROM train
UNION ALL
SELECT train_no, 'Business' AS class_name, 200 AS fare_per_seat, 150 AS seat_count
FROM train;
