INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES
('itachi', 'uchiha', 'itachiuchiha@example.com', NOW(), NOW()),
('kakashi', 'hataki', 'kakachihataki@example.com', NOW(), NOW()),
('naruto', 'uzumaki', 'narutouzumaki@example.com', NOW(), NOW());
select * from users;
select * from users where email = 'itachiuchiha@example.com';
select * from users where id = (select MAX(id) from users);
UPDATE users SET last_name = 'Pancakes', updated_at = NOW() WHERE id = 3;
DELETE FROM users WHERE id = 2;
SELECT * FROM users ORDER BY first_name ASC;
SELECT * FROM users ORDER BY first_name DESC;




