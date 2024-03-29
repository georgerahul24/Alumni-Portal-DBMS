DROP DATABASE IF EXISTS AlumniPortal;
CREATE DATABASE AlumniPortal;
USE AlumniPortal;

CREATE TABLE ProfileStatic
(
    rollNumber            INTEGER PRIMARY KEY,
    name                  VARCHAR(100) NOT NULL,

    /* Email IDs */
    instituteEmail        VARCHAR(100) NOT NULL,
    primaryEmail          VARCHAR(100)  DEFAULT NULL,
    showEmail             BOOLEAN       DEFAULT TRUE,
    CONSTRAINT instituteEmailConstraint CHECK (instituteEmail like '%@iiitg.ac.in'),
    CONSTRAINT primaryEmailConstraint CHECK (primaryEmail like '%@%'),

    /* Phone Numbers */
    primaryPhoneNumber    VARCHAR(15)  NOT NULL,
    secondaryPhoneNumber  VARCHAR(15)   DEFAULT NULL,
    showPhoneNumber       BOOLEAN       DEFAULT TRUE,

    /* College Specific Details */
    graduationYear        INTEGER      NOT NULL,
    degree                VARCHAR(100) NOT NULL,
    department            VARCHAR(50)  NOT NULL,
    DOB                   DATE         NOT NULL,

    /* Addresses */
    permanentCity         VARCHAR(250) NOT NULL,
    permanentState        VARCHAR(250) NOT NULL,
    permanentCountry      VARCHAR(250) NOT NULL,

    correspondenceCity    VARCHAR(250)  DEFAULT NULL,
    correspondenceState   VARCHAR(250)  DEFAULT NULL,
    correspondenceCountry VARCHAR(250)  DEFAULT NULL,
    showAddress           BOOLEAN       DEFAULT TRUE,

    /* Social Media Links */
    linkedin              VARCHAR(1000) DEFAULT NULL,
    github                VARCHAR(1000) DEFAULT NULL,
    twitter               VARCHAR(1000) DEFAULT NULL,

    password              varchar(100) NOT NULL


);

CREATE TABLE FirstLogin
(
    rollNumber INTEGER PRIMARY KEY,
    accessed   BOOLEAN DEFAULT FALSE,

    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber) ON DELETE CASCADE
);

CREATE TABLE Accomplishments
(
    rollNumber INTEGER      NOT NULL,
    title      VARCHAR(250) NOT NULL,
    body       VARCHAR(2000),
    month      INTEGER      NOT NULL,
    year       INTEGER      NOT NULL,

    CONSTRAINT monthAccomplishmentsConstraint CHECK ( month >= 1 AND month <= 12 ),
    CONSTRAINT yearAccomplishmentsConstraint CHECK ( year >= 1950 AND year <= 2030),

    PRIMARY KEY (rollNumber, title),
    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber) ON DELETE CASCADE
);

CREATE TABLE Institutes
(
    name        VARCHAR(250) PRIMARY KEY,
    city        VARCHAR(250) NOT NULL,
    state       VARCHAR(250) NOT NULL,
    country     VARCHAR(250) NOT NULL,
    yearStarted INTEGER      NOT NULL


);

CREATE TABLE Companies
(
    name        VARCHAR(250) PRIMARY KEY,
    city        VARCHAR(250) NOT NULL,
    state       VARCHAR(250) NOT NULL,
    country     VARCHAR(250) NOT NULL,
    yearStarted INTEGER      NOT NULL


);

CREATE TABLE Education
(
    rollNumber   INTEGER      NOT NULL,
    degree       VARCHAR(250) NOT NULL,
    fieldOfStudy VARCHAR(250) DEFAULT ' ',
    institute    VARCHAR(250) NOT NULL,
    description  VARCHAR(2000),
    startYear    INTEGER      NOT NULL,
    endYear      INTEGER      DEFAULT NULL,

    CONSTRAINT startYearEducationConstraint CHECK ( startYear >= 1950 AND startYear <= 2030 ),
    CONSTRAINT endYearEducationConstraint CHECK ( endYear >= 1950 AND endYear <= 2030),

    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber) ON DELETE CASCADE,
    PRIMARY KEY (rollNumber, degree, fieldOfStudy)
);

CREATE TABLE Experiences
(
    rollNumber  INTEGER      NOT NULL,
    title       VARCHAR(250) NOT NULL,
    companyName VARCHAR(250) not null,
    description TEXT,
    startMonth  INTEGER      NOT NULL,
    startYear   INTEGER      NOT NULL,
    endMonth    INTEGER DEFAULT NULL,
    endYear     INTEGER DEFAULT NULL,

    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber) ON DELETE CASCADE,
    -- FOREIGN KEY (companyName) REFERENCES Companies (name),
    PRIMARY KEY (rollNumber, companyName, startMonth, startYear),
    CONSTRAINT startMonthJobConstraint CHECK ( startMonth >= 1 AND startMonth <= 12 ),
    CONSTRAINT endMonthJobConstraint CHECK ( endMonth >= 1 AND endMonth <= 12 )


);

CREATE TABLE Stories
(
    rollNumber INTEGER      NOT NULL,
    title      VARCHAR(250) NOT NULL,
    datePosted DATETIME     NOT NULL,
    body       TEXT         NOT NULL,

    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber) ON DELETE CASCADE,
    PRIMARY KEY (rollNumber, title)

);

CREATE TABLE Ideas
(
    rollNumber  INTEGER      NOT NULL,
    title       VARCHAR(250) NOT NULL,
    datePosted  DATETIME     NOT NULL,
    description TEXT         NOT NULL,
    FOREIGN KEY (rollNumber) REFERENCES ProfileStatic (rollNumber) ON DELETE CASCADE,
    PRIMARY KEY (rollNumber, title)
)


