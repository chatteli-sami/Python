--  Create 5 different users: Jane Amsden, Emily Dixon, Theodore Dostoevsky, William Shapiro, Lao Xiu
INSERT INTO users (first_name, last_name) VALUES ('Jane', 'Amsden');
INSERT INTO users (first_name, last_name) VALUES ('Emily', 'Dixon');
INSERT INTO users (first_name, last_name) VALUES ('Theodore', 'Dostoevsky');
INSERT INTO users (first_name, last_name) VALUES ('William', 'Shapiro');
INSERT INTO users (first_name, last_name) VALUES ('Lao', 'Xiu');

-- Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books (title) VALUES ('C Sharp');
INSERT INTO books (title) VALUES ('Java');
INSERT INTO books (title) VALUES ('Python');
INSERT INTO books (title) VALUES ('PHP');
INSERT INTO books (title) VALUES ('Ruby');

--  Change the name of the C Sharp book to C#
UPDATE books SET title = 'C#' WHERE id = 1;

-- Change the first name of the 4th user to Bill
UPDATE users SET first_name = 'Bill' WHERE id = 4;

-- Have the first user favorite the first 2 books
INSERT INTO favorites (user_id, book_id) VALUES (1, 1);
INSERT INTO favorites (user_id, book_id) VALUES (1, 2);

--  Have the second user favorite the first 3 books
 INSERT INTO favorites (user_id, book_id) VALUES (2, 1);
INSERT INTO favorites (user_id, book_id) VALUES (2, 2);
INSERT INTO favorites (user_id, book_id) VALUES (2, 3);

-- Have the third user favorite the first 4 books
INSERT INTO favorites (user_id, book_id) VALUES (3, 1);
INSERT INTO favorites (user_id, book_id) VALUES (3, 2);
INSERT INTO favorites (user_id, book_id) VALUES (3, 3);
INSERT INTO favorites (user_id, book_id) VALUES (3, 4);

-- Have the fourth user favorite all the books
INSERT INTO favorites (user_id, book_id) VALUES (4, 1);
INSERT INTO favorites (user_id, book_id) VALUES (4, 2);
INSERT INTO favorites (user_id, book_id) VALUES (4, 3);
INSERT INTO favorites (user_id, book_id) VALUES (4, 4);
INSERT INTO favorites (user_id, book_id) VALUES (4, 5);

-- Retrieve all the users who favorited the 3rd book
SELECT users.* 
FROM users 
JOIN favorites ON users.id = favorites.user_id 
WHERE favorites.book_id = 3;

-- Remove the first user of the 3rd book's favorites
DELETE FROM favorites 
WHERE user_id = 1 AND book_id = 3;

-- Have the 5th user favorite the 2nd book
INSERT INTO favorites (user_id, book_id) VALUES (5, 2);

-- Find all the books that the 3rd user favorited
SELECT books.* 
FROM books 
JOIN favorites ON books.id = favorites.book_id 
WHERE favorites.user_id = 3;

-- Find all the users that favorited the 5th book
SELECT users.* 
FROM users 
JOIN favorites ON users.id = favorites.user_id 
WHERE favorites.book_id = 5;






