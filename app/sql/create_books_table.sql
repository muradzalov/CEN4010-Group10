CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(255),
    rating FLOAT,
    copies_sold INT,
    price FLOAT,
    publisher VARCHAR(255)
);
