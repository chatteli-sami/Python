-- Create 3 new dojos
insert into dojos (name) values ('naruto');
insert into dojos (name) values ('saseki');
insert into dojos (name) values ('kakachi');

-- Delete the 3 dojos you just created
SET SQL_SAFE_UPDATES = 0;
delete from dojos where name in ('naruto', 'saseki', 'kakachi');

-- Create 3 more dojos
insert into dojos (name) values ('kakachi');
insert into dojos (name) values ('asuma');
insert into dojos (name) values ('guyy');

-- Create 3 ninjas that belong to the first dojo
insert into ninjas (first_name, last_name, age, dojo_id) values ('naruto', 'uzumaki', 18, 1);
insert into ninjas (first_name, last_name, age, dojo_id) values ('saseki', 'uchiha', 18, 1);
insert into ninjas (first_name, last_name, age, dojo_id) values ('sakura', 'hakura', 17, 1);

-- Create 3 ninjas that belong to the second dojo
insert into ninjas (first_name, last_name, age, dojo_id) values ('tchuji', 'akemichi', 16, 2);
insert into ninjas (first_name, last_name, age, dojo_id) values ('nara', 'shikamru', 17, 2);
insert into ninjas (first_name, last_name, age, dojo_id) values ('ino', 'yamanaka', 18, 2);

-- Create 3 ninjas that belong to the third dojo
insert into ninjas (first_name, last_name, age, dojo_id) values ('niji', 'hygua', 19, 3);
insert into ninjas (first_name, last_name, age, dojo_id) values ('rok', 'ly', 15, 3);
insert into ninjas (first_name, last_name, age, dojo_id) values ('ten', 'ten', 20, 3);

-- Retrieve all the ninjas from the first dojo
select * from ninjas where dojo_id = 1;

-- Retrieve all the ninjas from the last dojo
select * from ninjas where dojo_id = 3;

-- Retrieve the last ninja's dojo
select * from dojos where id = (select dojo_id from ninjas order by id desc limit 1);

-- Use a JOIN to retrieve the ninja with id 6 as well as the data from its dojo. Be sure to do this in one query using a join statement.
select ninjas.*, dojos.* 
from ninjas 
join dojos on ninjas.dojo_id = dojos.id 
where ninjas.id = 6;

-- Use a JOIN to retrieve all the ninjas as well as that ninja's dojo, note, you will see repeated data on dojos as a dojo can have many ninjas!
select ninjas.*, dojos.* 
from ninjas 
join dojos on ninjas.dojo_id = dojos.id;



