DROP TABLE IF EXISTS user;

CREATE TABLE users (
    id INTEGER UNIQUE PRIMARY KEY,
    name TEXT NOT NULL,
    FOREIGN KEY courseId REFERENCES courses(id)
);

CREATE TABLE courses (
    id INTEGER UNIQUE PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE assignments (

    courseId INTEGER NOT NULL,
    name TEXT NOT NULL,
    id INTEGER PRIMARY KEY,
    FOREIGN KEY courseId REFERENCES courses(id)
);


CREATE TABLE parts (

    name TEXT NOT NULL,
    id INTEGER PRIMARY KEY
    FOREIGN KEY assignmentId REFERENCES assignments(id)
);
