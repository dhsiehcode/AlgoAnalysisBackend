
DROP TABLE IF EXISTS courses;

CREATE TABLE courses (
    id INTEGER UNIQUE PRIMARY KEY,
    name TEXT NOT NULL
);


DROP TABLE IF EXISTS users;


CREATE TABLE users (
    id INTEGER UNIQUE PRIMARY KEY,
    name TEXT NOT NULL,
    courseId INTEGER NOT NULL,
    FOREIGN KEY (courseId) REFERENCES courses(id)
);

DROP TABLE IF EXISTS assignments;

CREATE TABLE assignments (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    courseId INTEGER NOT NULL,
    FOREIGN KEY (courseId) REFERENCES courses(id)
);

DROP TABLE IF EXISTS parts;

CREATE TABLE parts (

    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    assignmentId INTEGER NOT NULL,
    courseId INTEGER NOT NULL,
    FOREIGN KEY (assignmentId) REFERENCES assignments(id)
    FOREIGN KEY (courseId) REFERENCES courses(id)
);
