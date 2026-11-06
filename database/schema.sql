-- HandIn database schema (SQLite)
-- Owner: Elvis. Anyone needing a change should ask Elvis or open a PR that he reviews.

DROP TABLE IF EXISTS submissions;
DROP TABLE IF EXISTS assignments;
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL,
    email         TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role          TEXT NOT NULL CHECK (role IN ('student', 'lecturer'))
);

CREATE TABLE courses (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    code        TEXT NOT NULL UNIQUE,
    title       TEXT NOT NULL,
    lecturer_id INTEGER NOT NULL REFERENCES users (id)
);

CREATE TABLE enrollments (
    student_id INTEGER NOT NULL REFERENCES users (id),
    course_id  INTEGER NOT NULL REFERENCES courses (id),
    PRIMARY KEY (student_id, course_id)
);

CREATE TABLE assignments (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id   INTEGER NOT NULL REFERENCES courses (id),
    title       TEXT NOT NULL,
    description TEXT,
    deadline    TEXT NOT NULL,                      -- 'YYYY-MM-DD HH:MM'
    created_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE submissions (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    assignment_id INTEGER NOT NULL REFERENCES assignments (id),
    student_id    INTEGER NOT NULL REFERENCES users (id),
    content       TEXT,                             -- typed answer
    file_path     TEXT,                             -- optional uploaded file
    submitted_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    grade         INTEGER CHECK (grade BETWEEN 0 AND 100),
    feedback      TEXT,
    UNIQUE (assignment_id, student_id)              -- one submission per student per assignment
);
