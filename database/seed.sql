-- Sample data for local development. All seed users have the password: password123

INSERT INTO users (id, name, email, password_hash, role) VALUES
 (1, 'Dr. Achieng Odhiambo', 'achieng@handin.test', 'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'lecturer'),
 (2, 'Mr. Otieno Kamau',     'otieno@handin.test',  'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'lecturer'),
 (3, 'Amina Hassan',         'amina@handin.test',   'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student'),
 (4, 'Brian Mutua',          'brian@handin.test',   'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student'),
 (5, 'Carol Wanjiru',        'carol@handin.test',   'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student');

INSERT INTO courses (id, code, title, lecturer_id) VALUES
 (1, 'CS101',  'Introduction to Programming', 1),
 (2, 'DB201',  'Database Systems',            2),
 (3, 'WEB210', 'Web Development',             2);

INSERT INTO enrollments (student_id, course_id) VALUES
 (3, 1), (3, 2),
 (4, 1), (4, 3),
 (5, 1), (5, 2), (5, 3);

INSERT INTO assignments (id, course_id, title, description, deadline) VALUES
 (1, 1, 'Lab 1: Variables and Loops',   'Solve the five exercises in the lab sheet.',  '2026-12-01 23:59'),
 (2, 1, 'Project Proposal',             'One page describing your project idea.',      '2026-10-15 23:59'),
 (3, 2, 'ER Diagram Exercise',          'Draw an ER diagram for a library system.',    '2026-12-05 23:59'),
 (4, 3, 'Build a Landing Page',         'Create a responsive landing page in HTML/CSS.', '2026-12-10 23:59');

INSERT INTO submissions (assignment_id, student_id, content, submitted_at, grade, feedback) VALUES
 (2, 3, 'My project idea is a campus ride-sharing app...', '2026-10-14 10:30', 78, 'Good scope. Add more detail on testing.'),
 (2, 4, 'I would like to build a study timetable planner...', '2026-10-15 20:10', NULL, NULL),
 (1, 3, 'Exercises 1 to 5 completed, see attached notes.', '2026-10-26 18:45', NULL, NULL);
