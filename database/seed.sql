-- Sample data for local development. All seed users have the password: password123

INSERT INTO users (id, name, email, reg_no, password_hash, role) VALUES
 (1,  'Dr. Achieng Odhiambo', 'achieng@handin.test', NULL,           'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'lecturer'),
 (2,  'Mr. Otieno Kamau',     'otieno@handin.test',  NULL,           'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'lecturer'),
 (3,  'Amina Hassan',         'amina@handin.test',   'SFE/2023/045', 'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student'),
 (4,  'Brian Mutua',          'brian@handin.test',   'SFE/2023/078', 'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student'),
 (5,  'Carol Wanjiru',        'carol@handin.test',   'SFE/2023/102', 'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student'),
 (6,  'Daniel Mutua',         'daniel@handin.test',  'SFE/2023/067', 'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student'),
 (7,  'Esther Nyakundi',      'esther@handin.test',  'SFE/2023/090', 'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student'),
 (8,  'James Fortune',        'james@handin.test',   'SFE/2023/056', 'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student'),
 (9,  'Kevin Otieno',         'kevin@handin.test',   'SFE/2023/072', 'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student'),
 (10, 'Lilian Njeri',         'lilian@handin.test',  'SFE/2023/083', 'pbkdf2:sha256:1000000$CXkuH6LLDjWKsYVn$b0c82b8e242c4c0f07260ef36852f149eeb76215a190618566c9e654b0373af2', 'student');

INSERT INTO courses (id, code, title, lecturer_id) VALUES
 (1, 'CS101',  'Introduction to Programming', 1),
 (2, 'DB201',  'Database Systems',            2),
 (3, 'WEB210', 'Web Development',             2);

INSERT INTO enrollments (student_id, course_id) VALUES
 (3, 1), (3, 2),
 (4, 1), (4, 3),
 (5, 1), (5, 2), (5, 3),
 (6, 1), (7, 1), (8, 1), (9, 1), (10, 1);

INSERT INTO assignments (id, course_id, title, description, deadline) VALUES
 (1, 1, 'Lab 1: Variables and Loops',   'Solve the five exercises in the lab sheet.',  '2026-12-01 23:59'),
 (2, 1, 'Project Proposal',             'One page describing your project idea.',      '2026-10-15 23:59'),
 (3, 2, 'ER Diagram Exercise',          'Draw an ER diagram for a library system.',    '2026-12-05 23:59'),
 (4, 3, 'Build a Landing Page',         'Create a responsive landing page in HTML/CSS.', '2026-12-10 23:59');

-- The first three rows keep their original order so existing ids (1, 2, 3) do not change.
INSERT INTO submissions (assignment_id, student_id, content, submitted_at, grade, feedback) VALUES
 (2, 3, 'My project idea is a campus ride-sharing app...', '2026-10-14 10:30', 78, 'Good scope. Add more detail on testing.'),
 (2, 4, 'I would like to build a study timetable planner...', '2026-10-15 20:10', NULL, NULL),
 (1, 3, 'Exercises 1 to 5 completed, see attached notes.', '2026-10-26 18:45', NULL, NULL),
 (2, 6, 'A library seat booking system for the campus.',   '2026-10-13 16:22', 65, 'Clear idea, needs a testing plan.'),
 (2, 7, 'A lost-and-found portal for students.',            '2026-10-14 08:45', NULL, NULL),
 (2, 8, 'An events notice board for clubs.',                '2026-10-15 11:37', NULL, NULL),
 (1, 6, 'Solutions to exercises 1 to 5.',                   '2026-10-27 09:14', NULL, NULL),
 (1, 10,'Lab 1 answers attached in the notes below.',       '2026-10-27 15:12', NULL, NULL);
