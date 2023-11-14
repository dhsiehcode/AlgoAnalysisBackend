DROP TABLE IF EXISTS user;

CREATE TABLE users (
    id TEXT UNIQUE PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT NOT NULL
);

CREATE TABLE courses (
    id TEXT UNIQUE PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE assignments (

    course

)
