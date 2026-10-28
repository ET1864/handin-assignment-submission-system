# HandIn: Student Assignment Submission System

A simple web system where students register, view their classes and assignments,
submit work and track submission status, and lecturers create assignments,
view submissions and grade them.

Built for SFE 4015 Software Configuration Management, Assignment 2 (Fall 2026).

## Features
- Student: register, log in, view classes, view pending work, submit, view submission status and grade
- Lecturer: log in, view classes taught, create assignments, view who submitted, view and grade submissions

## Tech stack
Python, Flask, SQLite, HTML/CSS. Everyone runs their own local copy; the database
is built from `database/schema.sql` and seed data.

## Team
| Member | Responsibility | Branches |
|--------|----------------|----------|
| Emmanuel | Foundation, register/login/logout, student "my classes", PR merging and release tags | `login-feature`, `student-dashboard` |
| Ted | Student class page, submit assignment, submission status, change request (edit submission) | `submission-feature`, `change-edit-submission` |
| Lewis | Lecturer classes, create assignment, who-submitted view, recovery demo | `lecturer-feature` |
| Elvis | Database schema and seed data, view and grade submissions, tests, requirements doc | `database-and-tests`, `grading-feature` |

## Branching strategy
- `main`: stable, working code only, releases are tagged here
- One branch per feature (see table above); `change-*` branches for change requests
- All merges into `main` go through a Pull Request reviewed by a teammate

## Commit message convention
A clear, specific, present-tense sentence, e.g. `Add student registration form and validation`.
Avoid messages like "update" or "changes".

## Running locally
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    flask --app app run

## Releases
See the Releases/Tags page of this repository.
