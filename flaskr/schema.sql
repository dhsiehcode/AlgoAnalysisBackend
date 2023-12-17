CREATE TABLE accounts (
    name TEXT PRIMARY KEY,
    hashed_password TEXT,
    classes TEXT,
);

CREATE TABLE projects (
    class TEXT PRIMARY KEY,
    class_id TEXT UNIQUE,
    name TEXT,
    vocareum_id TEXT,
);

CREATE TABLE tests (
    project TEXT PRIMARY KEY,
    test_file TEXT,
)