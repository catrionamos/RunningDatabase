--sql file used by the docker database container to create and fill the tables on first start

--main table holding the running programs
create table if not exists programs(
program_id varchar(10) not null primary key,
program_name varchar(100) not null,
target_level varchar(30),
duration_weeks int,
description varchar(255)
);

--users table, password is stored as a hash, each user can follow a program
create table if not exists users(
userid varchar(50) not null primary key,
password varchar(200) not null,
email varchar(120),
fitness_level varchar(30),
running_goal varchar(100),
program_id varchar(10),
foreign key (program_id) references programs(program_id)
);

--products sold in the shop
create table if not exists products(
product_id varchar(10) not null primary key,
product_name varchar(100) not null,
category varchar(50),
price float,
stock_quantity int
);

--runs logged by each user
create table if not exists runs(
run_id serial primary key,
userid varchar(50) not null,
run_date date,
distance_km float,
duration_minutes int,
notes varchar(255),
foreign key (userid) references users(userid)
);

--orders link users to the products they bought
create table if not exists orders(
order_id varchar(10) not null primary key,
userid varchar(50) not null,
product_id varchar(10) not null,
quantity int,
order_date date,
foreign key (userid) references users(userid),
foreign key (product_id) references products(product_id)
);

--insert data into the programs table
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p1', 'Couch to 5K', 'Beginner', 9, 'Run walk plan taking new runners from zero to 5km');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p2', '5K Speed Builder', 'Intermediate', 6, 'Interval sessions to improve your 5km time');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p3', '10K Foundation', 'Beginner', 10, 'Steady build up from 5km to 10km');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p4', '10K Performance', 'Intermediate', 8, 'Tempo and threshold work for a faster 10km');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p5', 'Half Marathon Intro', 'Intermediate', 12, 'First 21km plan with one long run each week');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p6', 'Half Marathon Endurance', 'Advanced', 12, 'Higher mileage plan for a half marathon PB');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p7', 'Marathon Base Builder', 'Intermediate', 16, 'Builds the weekly mileage needed for a marathon');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p8', 'Marathon Mastery', 'Advanced', 18, 'Full 42km plan with long runs and marathon pace work');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p9', 'Ultra 50K Starter', 'Advanced', 20, 'Trail and back to back long runs for a first ultra');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p10', 'Heart Rate Zone Training', 'All Levels', 6, 'Easy aerobic running using heart rate zones');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p11', 'Hill Repeats', 'Intermediate', 4, 'Weekly hill sessions for strength and power');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p12', 'Recovery and Mobility', 'All Levels', 4, 'Easy runs plus mobility to recover from a block');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p13', 'Trail Running Essentials', 'Beginner', 6, 'Technique and confidence for off road running');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p14', 'Sub 20 5K Challenge', 'Advanced', 8, 'Track sessions aimed at a sub 20 minute 5km');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p15', 'Sub 45 10K Challenge', 'Advanced', 8, 'Pace focused plan for a sub 45 minute 10km');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p16', 'Return to Running', 'Beginner', 6, 'Gentle plan for coming back after injury or a break');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p17', 'Run for Weight Loss', 'Beginner', 10, 'Frequent easy runs to build fitness and burn calories');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p18', 'Running Over 50', 'Beginner', 8, 'Joint friendly plan with extra rest days');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p19', 'Sprint and Agility', 'Intermediate', 4, 'Short fast efforts and drills for speed');
insert into programs(program_id, program_name, target_level, duration_weeks, description) values('p20', 'Winter Base Maintenance', 'All Levels', 8, 'Keeps your fitness ticking over in the off season');

--insert data into the users table, passwords are already hashed
insert into users(userid, password, email, fitness_level, running_goal, program_id) values('CatrionaRuns', 'scrypt:32768:8:1$jFfACojbINjkVIOG$c3d1d1f75eaf8dd64d284c5007e356b5caf5e2e8144e80742af008b4da352323f97133ca8d8e1c817f506a403528780b944ea474d357be95d38bd44480460612', 'catrionaruns@example.com', 'Intermediate', 'Sub 20 minute 5K', 'p14');
insert into users(userid, password, email, fitness_level, running_goal, program_id) values('JohnRunner', 'scrypt:32768:8:1$UA7EidxubaZikBhS$7d0a7a14774733bbeeac5f3aceffcf512ce42e706aaef48509aa10f8bc7eb30ee1db7439d9a734576df4d1a03ef579ea748d4bc156950ae979e983c0ed501f61', 'johnrunner@example.com', 'Beginner', 'Finish my first 5K', 'p1');
insert into users(userid, password, email, fitness_level, running_goal, program_id) values('SarahStrides', 'scrypt:32768:8:1$r3AoXVdAtxo3R2Fo$70fe302ee076fdc1da52cae0c50deb960e6459170bbf029c1e3b1cb2c7079ca86d9ca567f22d94862a99e15a63b45c4c02a83193104f386d96b5a35d8e543a1b', 'sarahstrides@example.com', 'Intermediate', 'Run a half marathon', 'p5');
insert into users(userid, password, email, fitness_level, running_goal, program_id) values('MarkMiles', 'scrypt:32768:8:1$CusT1tvgtQCIM0o3$67c796429ba44e2370dd0af57ec42806c4d38e84f3a81ba4d68cd9086d5023da688a2191ca87520423fb127c92b9e7dfb643c1f5daf645a70ee799a4e9662be5', 'markmiles@example.com', 'Advanced', 'Marathon under 3h30', 'p8');
insert into users(userid, password, email, fitness_level, running_goal, program_id) values('AoifeJogs', 'scrypt:32768:8:1$YcKXzVR3qmPZT0pu$5d11891b545088d78a0f33597198c3172d5e3844b0d4d89da2dfd5f8b2fa4b5a880e76a26b1d60133399382c0d3bb44671c25b08679351e0a1ebd3b5c4eb4077', 'aoifejogs@example.com', 'Beginner', 'Run 10K without stopping', 'p3');
insert into users(userid, password, email, fitness_level, running_goal, program_id) values('LiamPace', 'scrypt:32768:8:1$rtMRYvGwdikJXvrP$5970c5abdbff514e6897c92d5bff5cb28c29aeb40e7075c09294f57c424273b7ab5679966187c749a2821a2cfdd95cf07b831b2a189df64935d930a612ff36c6', 'liampace@example.com', 'Intermediate', '10K PB', 'p4');
insert into users(userid, password, email, fitness_level, running_goal, program_id) values('NiamhTrail', 'scrypt:32768:8:1$fJ6TIp3V4A8woGL9$f064d2fd12ef5b97a83a7df6086170923dccacbf017368b91c0e971190b72d7653bd6a940d1a713855b34e1c7ee90fd08478b3f4aea3f32c5d29a51d3d0c6f9f', 'niamhtrail@example.com', 'Beginner', 'Try trail running', 'p13');
insert into users(userid, password, email, fitness_level, running_goal, program_id) values('ConorLongRun', 'scrypt:32768:8:1$sklq3koXB017iOJt$39974681778f99d80d211d75587bb7f03e741c92953a06dca8e8f25f18712e964edafafdf6baaaa9401c76e4a9f7254438e75b597c309096e1a2de7518889615', 'conorlongrun@example.com', 'Advanced', 'First ultra', 'p9');
insert into users(userid, password, email, fitness_level, running_goal, program_id) values('EmmaEasy', 'scrypt:32768:8:1$9KZsZ7DEryS3JK8d$ad62431e469318718fc69515499f1f6ae78174b5ec600e4eacb18203aa49713e4a174d3912b44cae2231c89852fe02b9ee24cf74bda05239f5b622d326d0cc9a', 'emmaeasy@example.com', 'All Levels', 'Stay fit over winter', 'p20');
insert into users(userid, password, email, fitness_level, running_goal, program_id) values('DavidDash', 'scrypt:32768:8:1$qIip8mqmVfFF4Yww$c7f43035dd0a9c14694f0e2106ac18ca4be52e3626262fc5069c8460306d3ac26616f415a709e45604cbf98d305e0586dc4abfd3260be3d341b583cd6b5b3482', 'daviddash@example.com', 'Intermediate', 'Get faster over 5K', 'p2');

--insert data into the products table
insert into products(product_id, product_name, category, price, stock_quantity) values('pr1', 'Pro Trail Running Shoes', 'Footwear', 129.99, 15);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr2', 'Road Racing Shoes', 'Footwear', 149.99, 12);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr3', 'Everyday Trainers', 'Footwear', 89.99, 30);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr4', 'GPS Running Watch', 'Electronics', 199.99, 10);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr5', 'Heart Rate Chest Strap', 'Electronics', 59.99, 18);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr6', 'Wireless Running Earbuds', 'Electronics', 79.99, 20);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr7', 'Hydration Running Vest', 'Accessories', 49.99, 25);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr8', 'Handheld Water Bottle', 'Accessories', 14.99, 40);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr9', 'Running Belt', 'Accessories', 19.99, 35);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr10', 'Reflective Running Jacket', 'Clothing', 69.99, 14);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr11', 'Running Shorts', 'Clothing', 29.99, 50);
insert into products(product_id, product_name, category, price, stock_quantity) values('pr12', 'Compression Socks', 'Clothing', 16.99, 60);

--insert data into the runs table
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('CatrionaRuns', '2026-10-11', 16.6, 95, 'Hill repeats');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('JohnRunner', '2026-10-02', 5.7, 29, 'Trail loop');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('SarahStrides', '2026-10-09', 21.6, 118, 'Windy but finished');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('MarkMiles', '2026-10-07', 5.1, 29, 'Recovery jog');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('AoifeJogs', '2026-09-20', 16.4, 116, 'Felt good');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('LiamPace', '2026-10-11', 10.7, 65, 'Trail loop');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('NiamhTrail', '2026-10-29', 5.8, 40, 'Windy but finished');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('ConorLongRun', '2026-09-09', 3.7, 19, 'Trail loop');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('EmmaEasy', '2026-10-28', 8.7, 60, 'Recovery jog');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('DavidDash', '2026-09-03', 16.4, 101, 'Windy but finished');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('CatrionaRuns', '2026-09-08', 6.8, 33, 'Long run');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('JohnRunner', '2026-10-21', 12.9, 75, 'Tempo session');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('SarahStrides', '2026-10-28', 12.5, 86, 'Intervals on the track');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('MarkMiles', '2026-10-06', 13.0, 82, 'Intervals on the track');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('AoifeJogs', '2026-09-30', 5.1, 25, 'Long run');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('LiamPace', '2026-09-02', 16.8, 85, 'Hill repeats');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('NiamhTrail', '2026-09-01', 5.4, 30, 'Trail loop');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('ConorLongRun', '2026-10-11', 5.7, 33, 'Trail loop');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('EmmaEasy', '2026-09-07', 16.9, 112, 'Parkrun');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('DavidDash', '2026-10-21', 12.4, 60, 'Intervals on the track');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('CatrionaRuns', '2026-09-08', 6.1, 31, 'Tempo session');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('JohnRunner', '2026-09-15', 10.6, 51, 'Trail loop');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('SarahStrides', '2026-09-20', 21.2, 117, 'Easy run');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('MarkMiles', '2026-09-10', 6.6, 32, 'Hill repeats');
insert into runs(userid, run_date, distance_km, duration_minutes, notes) values('AoifeJogs', '2026-10-15', 10.5, 51, 'Windy but finished');

--insert data into the orders table
insert into orders(order_id, userid, product_id, quantity, order_date) values('o1', 'ConorLongRun', 'pr8', 1, '2026-11-01');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o2', 'JohnRunner', 'pr3', 1, '2026-09-14');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o3', 'AoifeJogs', 'pr8', 1, '2026-09-21');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o4', 'MarkMiles', 'pr9', 1, '2026-10-17');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o5', 'EmmaEasy', 'pr1', 1, '2026-11-07');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o6', 'JohnRunner', 'pr12', 1, '2026-10-04');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o7', 'SarahStrides', 'pr6', 1, '2026-09-29');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o8', 'MarkMiles', 'pr10', 1, '2026-09-25');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o9', 'NiamhTrail', 'pr12', 1, '2026-09-30');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o10', 'EmmaEasy', 'pr8', 1, '2026-10-16');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o11', 'CatrionaRuns', 'pr5', 1, '2026-10-31');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o12', 'MarkMiles', 'pr12', 2, '2026-10-15');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o13', 'LiamPace', 'pr6', 1, '2026-09-11');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o14', 'JohnRunner', 'pr4', 1, '2026-10-31');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o15', 'LiamPace', 'pr4', 1, '2026-11-01');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o16', 'ConorLongRun', 'pr11', 1, '2026-10-15');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o17', 'JohnRunner', 'pr7', 2, '2026-09-26');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o18', 'SarahStrides', 'pr7', 1, '2026-10-13');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o19', 'NiamhTrail', 'pr8', 1, '2026-10-22');
insert into orders(order_id, userid, product_id, quantity, order_date) values('o20', 'SarahStrides', 'pr3', 1, '2026-09-17');
