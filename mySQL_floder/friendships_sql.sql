-- Create 6 new users
INSERT INTO users (first_name, last_name) VALUES ('Amy', 'Giver');
INSERT INTO users (first_name, last_name) VALUES ('Eli', 'Byers');
INSERT INTO users (first_name, last_name) VALUES ('john', 'smith');
INSERT INTO users (first_name, last_name) VALUES ('alex', 'sandrias');
INSERT INTO users (first_name, last_name) VALUES ('Marky', 'Mark');
INSERT INTO users (first_name, last_name) VALUES ('Bobby', 'frenk');

-- Have user 1 be friends with user 2, 4 and 6
INSERT INTO friendship (user_id, friend_id) VALUES (1, 2);
INSERT INTO friendship (user_id, friend_id) VALUES (1, 4);
INSERT INTO friendship (user_id, friend_id) VALUES (1, 6);

-- Have user 2 be friends with user 1, 3 and 5
INSERT INTO friendship (user_id, friend_id) VALUES (2, 1);
INSERT INTO friendship (user_id, friend_id) VALUES (2, 3);
INSERT INTO friendship (user_id, friend_id) VALUES (2, 5);

-- Have user 3 be friends with user 2 and 5
INSERT INTO friendship (user_id, friend_id) VALUES (3, 2);
INSERT INTO friendship (user_id, friend_id) VALUES (3, 5);

-- Have user 4 be friends with user 3
INSERT INTO friendship (user_id, friend_id) VALUES (4, 3);

-- Have user 5 be friends with user 1 and 6
INSERT INTO friendship (user_id, friend_id) VALUES (5, 1);
INSERT INTO friendship (user_id, friend_id) VALUES (5, 6);

-- Have user 6 be friends with user 2 and 3
INSERT INTO friendship (user_id, friend_id) VALUES (6, 2);
INSERT INTO friendship (user_id, friend_id) VALUES (6, 3);

 --  Display the relationships created as shown in the table in the above image
 SELECT 
    users.first_name, 
    users.last_name, 
    user2.first_name AS friend_first_name, 
    user2.last_name AS friend_last_name 
FROM 
    users 
JOIN 
    friendship ON users.id = friendship.user_id 
LEFT JOIN 
    users AS user2 ON friendship.friend_id = user2.id;
    
-- NINJA Query: Return all users who are friends with the first user, make sure their names are displayed in results.
SELECT 
    user2.first_name, 
    user2.last_name 
FROM 
    users 
JOIN 
    friendship ON users.id = friendship.user_id 
LEFT JOIN 
    users AS user2 ON friendship.friend_id = user2.id 
WHERE 
    users.id = 1;

-- NINJA Query: Return the count of all friendships
SELECT 
    COUNT(*) AS total_friendship
FROM 
    friendship;

-- NINJA Query: Find out who has the most friends and return the count of their friends.
SELECT 
    users.first_name, 
    users.last_name, 
    COUNT(friendship.friend_id) AS friend_count 
FROM 
    users 
JOIN 
    friendship ON users.id = friendship.user_id 
GROUP BY 
    users.id 
ORDER BY 
    friend_count DESC 
LIMIT 1;

-- NINJA Query: Return the friends of the third user in alphabetical order
SELECT 
    user2.first_name, 
    user2.last_name 
FROM 
    users 
JOIN 
    friendship ON users.id = friendship.user_id 
LEFT JOIN 
    users AS user2 ON friendship.friend_id = user2.id 
WHERE 
    users.id = 3 
ORDER BY 
    user2.first_name, 
    user2.last_name;








