INSERT INTO Student (student_id, name, login_duration, login_date, login_time, email) VALUES
(1, 'Wang', '00:00:00', '2021-01-01', '00:00:00', '034@qq.com'),
(2, 'Liu', '00:00:00', '2021-01-01', '00:00:00', '58@gmail.com'),
(3, 'Yuan', '00:00:00', '2021-01-01', '00:00:00', '67@gmail.com'),
(4, 'F Z', '00:00:00', '2021-01-01', '00:00:00', 'ku@gmail.com'),
(5, 'Feng', '00:00:00', '2021-01-01', '00:00:00', '18@gmail.com');


INSERT INTO Course (course_id, course_name, course_time, course_endTime, course_venue, assignment_ddl) VALUES
(1, "Database Management", '2021-04-23 13:30:00', '2021-04-23 13:45:00', 'online', '2021-04-23 09:30:00' ),
(2, "Java Programming", '2021-04-25 15:30:00', '2021-04-25 16:30:00', 'CPD 2-30', '2021-04-30 10:30:00'),
(3, "Game Design", '2021-04-26 13:30:00', '2021-04-26 14:30:00', 'CPD 1-24', '2021-04-25 13:30:00'),
(4, "Python", '2021-04-28 14:00:00', '2021-04-28 15:00:00', 'CPD 2-30', '2021-04-21 10:30:00');


INSERT INTO Teacher (name, email) VALUES
('Dr.Pi Luo', 'pluo@cs.hku.hk'),
('Jinan Wu','wjn922@connect.hku.hk'),
('A','A@cs.hku.hk'),
('B','B@cs.hku.hk'),
('C','C@cs.hku.hk'),
('D','D@cs.hku.hk');

INSERT INTO TAKE (take_id,course_id,student_id) VALUES
(1,1,1),
(2,2,1),
(3,3,1);



INSERT INTO Lecturer (name) VALUES
('Dr.Pig Luo'),
('A'),
('C');

INSERT INTO Tutor (name) VALUES
('Jiannan Wu'),
('B'),
('D');

INSERT INTO Lecture (course_id,zoom_link, lecturer_name) VALUES
(1,'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09','Dr.Ping Luo'),
(2,'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09','A'),
(3,'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09','A'),
(4,'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09','C');

INSERT INTO LectureNotes (course_id,LECTURENOTE_ID,lecture_notes) VALUES
(1,1, 'https://docs.qq.com/pdf/DWXN6cW1GRnNURVNy'),
(2,1, 'https://docs.qq.com/pdf/DWXN6cW1GRnNURVNy'),
(3,1, 'https://docs.qq.com/pdf/DWXN6cW1GRnNURVNy'),
(4,1, 'https://docs.qq.com/pdf/DWXN6cW1GRnNURVNy');

INSERT INTO Tutorial (course_id, session_id, course_time, course_endTime, zoom_link, tutor_name) VALUES
(1,1, '2021-04-14 09:30:00', '2021-04-14 10:30:00', 'https://hku.zoom.com.cn/j/2640918958?pwd=UmFpek1YMkUzNTFoL0ljRW84M1VLUT09', 'Jiannan Wu'),
(2,1, '2021-04-17 10:30:00', '2021-04-17 11:30:00', 'https://hku.zoom.com.cn/j/2640918958?pwd=UmFpek1YMkUzNTFoL0ljRW84M1VLUT09', 'B'),
(3,1, '2021-04-18 13:30:00', '2021-04-18 14:30:00', 'https://hku.zoom.com.cn/j/2640918958?pwd=UmFpek1YMkUzNTFoL0ljRW84M1VLUT09', 'D');

INSERT INTO TutorialNotes (course_id, note_id,tutorial_notes) VALUES
(1,1, 'https://docs.qq.com/pdf/DWXN6cW1GRnNURVNy'),
(2,1, 'https://docs.qq.com/pdf/DWXN6cW1GRnNURVNy'),
(3,1, 'https://docs.qq.com/pdf/DWXN6cW1GRnNURVNy');
