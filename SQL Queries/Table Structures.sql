CREATE DATABASE AlumniPortal;
USE AlumniPortal;

CREATE TABLE ProfileStatic
(
    rollNumber            INTEGER PRIMARY KEY,

    /* Email IDs */
    instituteEmail        VARCHAR(100),
    primaryEmail          VARCHAR(100),
    showEmail             BOOLEAN,
    CONSTRAINT instituteEmailConstraint CHECK (instituteEmail like '%@iiitg.ac.in'),
    CONSTRAINT primaryEmailConstraint CHECK (primaryEmail like '%@iiitg.ac.in'),

    /* Phone Numbers */
    primaryPhoneNumber    INTEGER,
    secondaryPhoneNumber  INTEGER,
    showPhoneNumber       BOOLEAN,

    /* College Specific Details */
    graduationYear        INTEGER,
    degree                VARCHAR(100),
    department            VARCHAR(50),

    DOB                   DATE,

    /* Addresses */
    permanentAddress      VARCHAR(100),
    correspondenceAddress VARCHAR(100),
    showAddress           BOOLEAN,

    /* Social Media Links */
    linkedin              VARCHAR(1000),
    github                VARCHAR(1000),
    twitter               VARCHAR(1000),

    password              varchar(100),
    photo                 MEDIUMBLOB


);

CREATE TABLE FirstLogin
(
    rollNumber INTEGER PRIMARY KEY,
    accessed   BOOLEAN,

    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber)
);

CREATE TABLE Accomplishments
(
    rollNumber INTEGER PRIMARY KEY,
    title      VARCHAR(250),
    body       TEXT,
    month      INTEGER,
    year       INTEGER,

    CONSTRAINT monthAccomplishmentsConstraint CHECK ( month >= 1 AND month <= 12 ),
    CONSTRAINT yearAccomplishmentsConstraint CHECK ( year >= 1950 AND year <= 2030),
    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber) ON DELETE CASCADE
);

CREATE TABLE Institutes
(
    name        VARCHAR(250) PRIMARY KEY,
    city        VARCHAR(250),
    state       VARCHAR(250),
    country     VARCHAR(250),
    yearStarted INTEGER


);

CREATE TABLE Companies
(
    name        VARCHAR(250) PRIMARY KEY,
    city        VARCHAR(250),
    state       VARCHAR(250),
    country     VARCHAR(250),
    yearStarted INTEGER


);

CREATE TABLE Education
(
    rollNumber   INTEGER,
    degree       VARCHAR(250),
    fieldOfStudy VARCHAR(250),
    institute    VARCHAR(250),
    title        VARCHAR(250),
    description  TEXT,
    startYear    INTEGER,
    endYear      INTEGER,

    CONSTRAINT startYearEducationConstraint CHECK ( startYear >= 1950 AND startYear <= 2030 ),
    CONSTRAINT endYearEducationConstraint CHECK ( endYear >= 1950 AND endYear <= 2030),

    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber) ON DELETE CASCADE,
    FOREIGN KEY (institute) REFERENCES Institutes (name),
    PRIMARY KEY (rollNumber, institute, degree, fieldOfStudy)
);

CREATE TABLE JobProfile
(
    rollNumber  INTEGER,
    title       VARCHAR(250),
    companyName VARCHAR(250),
    description TEXT,
    startDate   DATE,
    endDate     DATE,

    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber) ON DELETE CASCADE,
    FOREIGN KEY (companyName) REFERENCES Institutes (name),
    PRIMARY KEY (rollNumber, companyName, startDate)


);

CREATE TABLE Stories
(
    rollNumber INTEGER,
    title      VARCHAR(250),
    datePosted DATETIME,
    body       TEXT,

    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber),
    PRIMARY KEY (rollNumber, title)

);

CREATE TABLE Ideas
(
    rollNumber  INTEGER,
    title       VARCHAR(250),
    datePosted  DATETIME,
    description TEXT,
    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber),
    PRIMARY KEY (rollNumber, title)
)


