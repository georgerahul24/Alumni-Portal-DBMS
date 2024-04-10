INSERT INTO ProfileStatic (rollNumber, name, instituteEmail, primaryEmail, showEmail, primaryPhoneNumber, secondaryPhoneNumber, showPhoneNumber, graduationYear, degree, department, DOB, permanentCity, permanentState, permanentCountry, correspondenceCity, correspondenceState, correspondenceCountry, showAddress, linkedin, github, twitter, password) VALUES
(2001001, 'Aarav Singh', 'aarav.singh@iiitg.ac.in', 'aarav@gmail.com', TRUE, '9123456780', NULL, TRUE, 2020, 'B.Tech', 'Computer Science and Engineering', '2001-09-15', 'Guwahati', 'Assam', 'India', 'Guwahati', 'Assam', 'India', TRUE, 'linkedin.com/in/aarav', 'github.com/aarav', NULL, 'password123'),

(2001002, 'Isha Patil', 'isha.patil@iiitg.ac.in', 'isha@gmail.com', TRUE, '9234567891', '9123456789', TRUE, 2020, 'B.Tech', 'Electronics and Communication Engineering', '2002-08-22', 'Pune', 'Maharashtra', 'India', NULL, NULL, NULL, FALSE, 'linkedin.com/in/isha', NULL, 'twitter.com/isha', 'password456'),

(2001003, 'Rohan Kumar', 'rohan.kumar@iiitg.ac.in', NULL, FALSE, '9345678902', NULL, FALSE, 2020, 'B.Tech', 'Computer Science and Engineering', '2001-07-11', 'Patna', 'Bihar', 'India', 'Patna', 'Bihar', 'India', TRUE, NULL, 'github.com/rohankumar', NULL, 'securePass789'),

(2001004, 'Anjali Rao', 'anjali.rao@iiitg.ac.in', 'anjali@gmail.com', TRUE, '9456789012', NULL, TRUE, 2020, 'B.Tech', 'Electronics and Communication Engineering', '2002-05-30', 'Hyderabad', 'Telangana', 'India', 'Hyderabad', 'Telangana', 'India', TRUE, 'linkedin.com/in/anjalirao', NULL, 'twitter.com/anjalirao', 'password321'),

(2001005, 'Soham Shah', 'soham.shah@iiitg.ac.in', 'soham@gmail.com', TRUE, '9567890123', '9345678901', TRUE, 2020, 'B.Tech', 'Computer Science and Engineering', '2001-12-16', 'Ahmedabad', 'Gujarat', 'India', NULL, NULL, NULL, FALSE, NULL, 'github.com/sohamshah', NULL, 'pass123456'),

(2001006, 'Priya Malik', 'priya.malik@iiitg.ac.in', NULL, FALSE, '9678901234', NULL, FALSE, 2020, 'B.Tech', 'Electronics and Communication Engineering', '2002-04-08', 'Kolkata', 'West Bengal', 'India', 'Kolkata', 'West Bengal', 'India', TRUE, 'linkedin.com/in/priyamalik', NULL, NULL, 'password654'),

(2001007, 'Vikram Aditya', 'vikram.aditya@iiitg.ac.in', 'vikram@gmail.com', TRUE, '9789012345', '9567890123', TRUE, 2020, 'B.Tech', 'Computer Science and Engineering', '2001-02-20', 'Chennai', 'Tamil Nadu', 'India', NULL, NULL, NULL, FALSE, NULL, 'github.com/vikramaditya', 'twitter.com/vikramaditya', 'pass987654'),

(2001008, 'Sneha Mohan', 'sneha.mohan@iiitg.ac.in', 'sneha@gmail.com', TRUE, '9890123456', NULL, TRUE, 2020, 'B.Tech', 'Electronics and Communication Engineering', '2002-01-26', 'Kochi', 'Kerala', 'India', 'Kochi', 'Kerala', 'India', TRUE, 'linkedin.com/in/snehamohan', NULL, NULL, 'password789123'),

(2001009, 'Ritvik Sharma', 'ritvik.sharma@iiitg.ac.in', NULL, FALSE, '9901234567', '9789012345', TRUE, 2020, 'B.Tech', 'Computer Science and Engineering', '2001-03-19', 'Jaipur', 'Rajasthan', 'India', NULL, NULL, NULL, FALSE, NULL, NULL, 'twitter.com/ritviksharma', 'secure789pass'),

(2001010, 'Neha Singh', 'neha.singh@iiitg.ac.in', 'neha@gmail.com', TRUE, '9012345678', NULL, TRUE, 2020, 'B.Tech', 'Electronics and Communication Engineering', '2002-11-05', 'Lucknow', 'Uttar Pradesh', 'India', 'Lucknow', 'Uttar Pradesh', 'India', TRUE, 'linkedin.com/in/nehasingh', 'github.com/nehasingh', NULL, 'password123secure');


INSERT INTO FirstLogin (rollNumber, accessed) VALUES
(2001001, FALSE),
(2001002, FALSE),
(2001003, FALSE),
(2001004, FALSE),
(2001005, FALSE),
(2001006, FALSE),
(2001007, FALSE),
(2001008, FALSE),
(2001009, FALSE),
(2001010, FALSE);

INSERT INTO Accomplishments (rollNumber, title, body, month, year) VALUES
(2001001, 'Hackathon Winner', 'Won first place at the National Coding Hackathon, showcasing exceptional problem-solving skills.', 9, 2022),
(2001001, 'Published Research', 'Co-authored a paper on blockchain technology that was published in a prestigious tech journal.', 4, 2023),
(2001002, 'Best Design Project', 'Awarded best design project in the annual university project showcase for an innovative solar-powered device.', 5, 2022),
(2001002, 'Debate Champion', 'Led the college debate team to victory at a national debate competition.', 11, 2021),
(2001003, 'Internship at Tech Giant', 'Completed a challenging summer internship at Google, working on machine learning models.', 7, 2021),
(2001003, 'AI for Good Challenge', 'Won second place in the "AI for Good" global challenge for developing an AI to predict natural disasters.', 2, 2023),
(2001004, 'Youth Leadership Conference', 'Represented the university at the International Youth Leadership Conference in Dubai.', 3, 2022),
(2001004, 'Robotics Club President', 'Served as the president of the university’s robotics club, leading the team to a national championship.', 9, 2021),
(2001005, 'App Innovation Award', 'Developed a health tracking app that won the National App Innovation Award.', 8, 2022),
(2001005, 'Chess Tournament Winner', 'Won the inter-college chess tournament, demonstrating strategic thinking and resilience.', 10, 2020),
(2001006, 'Science Fair Gold Medal', 'Awarded the gold medal in the state science fair for a project on sustainable energy solutions.', 12, 2021),
(2001006, 'Volunteer of the Year', 'Named Volunteer of the Year by a local non-profit for outstanding community service.', 4, 2022),
(2001007, 'Startup Accelerator Winner', 'Co-founded a tech startup that won first place in a prominent startup accelerator program.', 6, 2023),
(2001007, 'Photography Contest', 'Received first place in a national photography contest with a portfolio on urban landscapes.', 7, 2020),
(2001008, 'Engineering Excellence Scholarship', 'Received a prestigious scholarship for demonstrating exceptional talent in engineering.', 1, 2022),
(2001008, 'Marathon Finisher', 'Completed a full marathon, showcasing determination and physical endurance.', 5, 2021),
(2001009, 'Peer Tutoring Award', 'Recognized for contributions to the university’s peer tutoring program, helping hundreds of students succeed academically.', 3, 2023),
(2001009, 'Outdoor Adventure Leader', 'Led a group of students on a challenging outdoor adventure trip, enhancing teamwork and leadership skills.', 8, 2022),
(2001010, 'Innovative Solution Prize', 'Awarded a prize for an innovative solution to reduce water wastage on campus.', 11, 2022),
(2001010, 'Music Competition First Place', 'Won first place in a regional music competition, playing classical guitar.', 4, 2021);

INSERT INTO Institutes (name, city, state, country, yearStarted) VALUES
('Indian Institute of Technology Delhi', 'New Delhi', 'Delhi', 'India', 1961),
('Indian Institute of Information Technology, Guwahati', 'Guwahati', 'Assam', 'India', 2013),
('Indian Institute of Technology Madras', 'Chennai', 'Tamil Nadu', 'India', 1959),
('National Institute of Technology Tiruchirappalli', 'Tiruchirappalli', 'Tamil Nadu', 'India', 1964),
('National Institute of Technology Surathkal', 'Mangalore', 'Karnataka', 'India', 1960),
('California Institute of Technology', 'Pasadena', 'California', 'USA', 1891),
('University of Cambridge', 'Cambridge', 'Cambridgeshire', 'United Kingdom', 1209),
('University of Oxford', 'Oxford', 'Oxfordshire', 'United Kingdom', 1096),
('Indian Institute of Technology Bombay', 'Mumbai', 'Maharashtra', 'India', 1958),
('National Institute of Technology Warangal', 'Warangal', 'Telangana', 'India', 1959),
('Princeton University', 'Princeton', 'New Jersey', 'USA', 1746),
('Carnegie Mellon University', 'Pittsburgh', 'Pennsylvania', 'USA', 1900),
('Harvard University', 'Cambridge', 'Massachusetts', 'USA', 1636),
('Massachusetts Institute of Technology', 'Cambridge', 'Massachusetts', 'USA', 1861),
('Stanford University', 'Stanford', 'California', 'USA', 1885);

INSERT INTO Companies (name, city, state, country, yearStarted) VALUES
('Amazon', 'Seattle', 'Washington', 'USA', 1994),
('Microsoft', 'Hyderabad', 'Telangana', 'India', 1975),
('Google', 'Hyderabad', 'Telangana', 'India', 1998),
('Capgemini', 'Mumbai', 'Maharashtra', 'India', 1967),
('American Express', 'Gurugram', 'Haryana', 'India', 1850),
('Atlassian', 'Bengaluru', 'Karnataka', 'India', 2002),
('HCL Technologies', 'Noida', 'Uttar Pradesh', 'India', 1976),
('JP Morgan Chase', 'Mumbai', 'Maharashtra', 'India', 2000),
('Flipkart', 'Bangalore', 'Karnataka', 'India', 2007),
('Netflix', 'Mumbai', 'Maharashtra', 'India', 1997),
('Oracle', 'Bengaluru', 'Karnataka', 'India', 1977),
('Deloitte', 'Hyderabad', 'Telangana', 'India', 1845),
('Wipro', 'Bangalore', 'Karnataka', 'India', 1945),
('Adobe', 'Noida', 'Uttar Pradesh', 'India', 1982),
('Facebook', 'Hyderabad', 'Telangana', 'India', 2004),
('IBM', 'Bengaluru', 'Karnataka', 'India', 1911),
('Intel', 'Bengaluru', 'Karnataka', 'India', 1968),
('Salesforce', 'Hyderabad', 'Telangana', 'India', 1999),
('Spotify', 'Mumbai', 'Maharashtra', 'India', 2006),
('Twitter', 'Bengaluru', 'Karnataka', 'India', 2006),
('Uber', 'Bengaluru', 'Karnataka', 'India', 2009),
('Visa', 'Bengaluru', 'Karnataka', 'India', 1958),
('Samsung Electronics', 'Noida', 'Uttar Pradesh', 'India', 1969),
('Siemens', 'Mumbai', 'Maharashtra', 'India', 1847);

INSERT INTO Education (rollNumber, degree, fieldOfStudy, institute, description, startYear, endYear) VALUES
(2001001, 'B.Tech', 'Computer Science and Engineering', 'Indian Institute of Information Technology, Guwahati', 'Bachelor of Technology in Computer Science and Engineering', 2020, 2024),
(2001002, 'B.Tech', 'Electronics and Communication Engineering', 'Indian Institute of Information Technology, Guwahati', 'Bachelor of Technology in Electronics and Communication Engineering', 2020, 2024),
(2001003, 'B.Tech', 'Computer Science and Engineering', 'Indian Institute of Information Technology, Guwahati', 'Bachelor of Technology in Computer Science and Engineering', 2020, 2024),
(2001004, 'B.Tech', 'Electronics and Communication Engineering', 'Indian Institute of Information Technology, Guwahati', 'Bachelor of Technology in Electronics and Communication Engineering', 2020, 2024),
(2001005, 'B.Tech', 'Computer Science and Engineering', 'Indian Institute of Information Technology, Guwahati', 'Bachelor of Technology in Computer Science and Engineering', 2020, 2024),
(2001006, 'B.Tech', 'Electronics and Communication Engineering', 'Indian Institute of Information Technology, Guwahati', 'Bachelor of Technology in Electronics and Communication Engineering', 2020, 2024),
(2001007, 'B.Tech', 'Computer Science and Engineering', 'Indian Institute of Information Technology, Guwahati', 'Bachelor of Technology in Computer Science and Engineering', 2020, 2024),
(2001008, 'B.Tech', 'Electronics and Communication Engineering', 'Indian Institute of Information Technology, Guwahati', 'Bachelor of Technology in Electronics and Communication Engineering', 2020, 2024),
(2001009, 'B.Tech', 'Computer Science and Engineering', 'Indian Institute of Information Technology, Guwahati', 'Bachelor of Technology in Computer Science and Engineering', 2020, 2024),
(2001010, 'B.Tech', 'Electronics and Communication Engineering', 'Indian Institute of Information Technology, Guwahati', 'Bachelor of Technology in Electronics and Communication Engineering', 2020, 2024),
(2001002, 'M.Tech', 'Computer Science and Engineering', 'Indian Institute of Technology Bombay', 'Master of Technology in Computer Science and Engineering', 2024, NULL),
(2001005, 'M.S.', 'Artificial Intelligence', 'Stanford University', 'Master of Science in Artificial Intelligence', 2024, NULL),
(2001007, 'MBA', 'Technology Management', 'Harvard University', 'Master of Business Administration in Technology Management', 2024, NULL);

INSERT INTO Experiences
(rollNumber, title, companyName, description, startMonth, startYear) VALUES
(2001001, 'Software Engineer', 'Google', 'Developing scalable web applications.', '01','2024'),
(2001003, 'Systems Analyst', 'Microsoft', 'Analyzing system requirements and overseeing network infrastructure.', '01','2024'),
(2001004, 'Data Scientist', 'Amazon', 'Leveraging large data sets to improve product recommendations.', '01','2024'),
(2001006, 'Network Engineer', 'Oracle', 'Designing and implementing new network solutions.', '01','2024'),
(2001008, 'Product Manager', 'Flipkart', 'Overseeing product development from conception to launch.', '01','2024'),
(2001009, 'UI/UX Designer', 'Adobe', 'Designing user interfaces and user experiences for mobile and web applications.', '01','2024'),
(2001010, 'Cybersecurity Analyst', 'IBM', 'Protecting company’s information systems from cyber threats.', '01','2024');



INSERT INTO Stories (rollNumber, title, datePosted, body) VALUES
(2001001, 'My First Hackathon Experience', '2023-03-15 10:30:00', 'Participating in my first hackathon was an exhilarating experience. The 36-hour coding spree not only pushed me to my limits but also taught me the importance of teamwork and perseverance. We didn''t win, but the learning was immense.'),
(2001002, 'Internship at a Startup', '2023-06-20 09:45:00', 'This summer, I interned at a tech startup focused on developing AI for healthcare. The opportunity to work on real-world problems and contribute to solutions that could potentially save lives was incredibly rewarding.'),
(2001004, 'Study Abroad Semester', '2023-11-05 14:00:00', 'Spending a semester abroad in Germany was one of the most enriching experiences of my life. Immersing myself in a different culture, learning a new language, and making friends from all over the world has broadened my perspective in ways I had never imagined.'),
(2001007, 'Volunteering for Social Good', '2023-08-12 16:30:00', 'This year, I volunteered with an NGO that aims to bridge the educational gap for underprivileged children. Teaching basic computer skills and witnessing their enthusiasm and quick learning was profoundly impactful. It''s something I plan to continue.'),
(2001009, 'My First Tech Conference', '2023-05-22 13:20:00', 'Attending my first tech conference as a speaker was a milestone. Sharing my project on stage in front of experienced professionals and receiving constructive feedback was a nerve-wracking yet amazing experience. Networking with like-minded individuals opened up new doors for collaboration.');


INSERT INTO Ideas (rollNumber, title, datePosted, description) VALUES
(2001002, 'Green Campus Initiative', '2023-09-10 15:00:00', 'To enhance sustainability and reduce our carbon footprint, I propose the Green Campus Initiative. This project will involve increasing the number of trees on campus, setting up solar panels to generate renewable energy, and implementing a comprehensive recycling program.'),
(2001003, 'Tech Mentorship Program', '2023-07-21 10:30:00', 'I suggest starting a Tech Mentorship Program that pairs upper-year students with first-year students. This program will not only help new students acclimate to the rigorous academic environment but also foster a sense of community. Senior students can share their experiences, provide guidance on academic and project work, and offer career advice.'),
(2001005, 'Mental Health Awareness Week', '2023-08-15 11:45:00', 'Mental health is crucial for academic success and overall well-being. I propose organizing an annual Mental Health Awareness Week featuring workshops, guest speakers, and activities focused on stress management, mindfulness, and mental health resources.'),
(2001008, 'Innovation Hub', '2023-10-02 09:30:00', 'To encourage creativity and innovation among students, I propose the creation of an Innovation Hub. This space will be equipped with the latest technology, including 3D printers, VR equipment, and software development kits, providing students with the tools they need to bring their ideas to life.'),
(2001010, 'Alumni Interaction Platform', '2023-12-01 12:00:00', 'Building a strong network is essential for personal and professional growth. I suggest developing an Alumni Interaction Platform that facilitates networking, mentorship, and collaboration between current students and alumni. This platform can host virtual meetups, mentorship programs, and forums for sharing job opportunities.');
