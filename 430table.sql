CREATE TABLE `Student` (
  `student_id` int(20) NOT NULL PRIMARY KEY,
  `name` varchar(50) NOT NULL,
  `login_duration` time NOT NULL,
  `login_date` date NOT NULL,
  `login_time` time NOT NULL,
  email varchar(50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Course (
  course_id INT NOT NULL PRIMARY KEY,
  course_name varchar(80) NOT NULL,
  course_time datetime NOT NULL,
  course_endTime datetime NOT NULL,
  course_venue varchar(80) NOT NULL,
  assignment_ddl datetime NOT NULL
);

CREATE TABLE Teacher (
  name varchar(50) NOT NULL PRIMARY KEY,
  email varchar(50) NOT NULL
);

CREATE TABLE TAKE (
  take_id INT NOT NULL PRIMARY KEY,
  course_id INT NOT NULL,
  student_id INT NOT NULL,
  FOREIGN KEY (course_id) REFERENCES Course (course_id),
  FOREIGN KEY (student_id) REFERENCES Student (student_id)
);

CREATE TABLE Lecturer (
  name varchar(50) NOT NULL PRIMARY KEY,
  FOREIGN KEY (name) REFERENCES Teacher (name)
);

CREATE TABLE Tutor (
  name varchar(50) NOT NULL PRIMARY KEY,
  FOREIGN KEY (name) REFERENCES Teacher (name)
);


CREATE TABLE Lecture (
  course_id INT NOT NULL PRIMARY KEY,
  zoom_link VARCHAR(2083) NOT NULL,
  lecturer_name varchar(50) NOT NULL,
  FOREIGN KEY (course_id) REFERENCES Course (course_id),
  FOREIGN KEY (lecturer_name) REFERENCES Lecturer (name)
);

CREATE TABLE LectureNotes (
  course_id INT NOT NULL,
  LECTURENOTE_ID INT NOT NULL,
  lecture_notes VARCHAR(2083) NOT NULL,
  PRIMARY KEY (course_id, LECTURENOTE_ID),
  FOREIGN KEY (course_id) REFERENCES Lecture (course_id)
);

CREATE TABLE Tutorial (
  course_id INT NOT NULL,
  session_id INT NOT NULL,
  course_time datetime NOT NULL,
  course_endTime datetime NOT NULL,
  zoom_link VARCHAR(2083) NOT NULL,
  tutor_name varchar(50) NOT NULL,
  PRIMARY KEY (course_id, session_id),
  FOREIGN KEY (course_id) REFERENCES Course (course_id),
  FOREIGN KEY (tutor_name) REFERENCES Tutor (name)
);

CREATE TABLE TutorialNotes (
  course_id INT NOT NULL,
  note_id INT NOT NULL,
  tutorial_notes VARCHAR(2083) NOT NULL,
  PRIMARY KEY (course_id, note_id),
  FOREIGN KEY (course_id) REFERENCES Tutorial (course_id)
);
