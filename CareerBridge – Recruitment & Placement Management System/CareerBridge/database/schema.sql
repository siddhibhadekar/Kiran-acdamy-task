CREATE DATABASE IF NOT EXISTS careerbridge CHARACTER SET utf8mb4;
USE careerbridge;

CREATE TABLE users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL,
  email VARCHAR(120) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('Admin','Recruiter','Placement Officer') NOT NULL
);
CREATE TABLE companies (
  company_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL, industry VARCHAR(80) NOT NULL, website VARCHAR(150),
  location VARCHAR(80) NOT NULL, hr_name VARCHAR(80) NOT NULL, hr_email VARCHAR(120) NOT NULL,
  hr_mobile VARCHAR(15), company_type ENUM('MNC','Startup','Mid-size','Consultancy') NOT NULL,
  status ENUM('ACTIVE','INACTIVE') DEFAULT 'ACTIVE'
);
CREATE TABLE candidates (
  candidate_id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(100) NOT NULL, email VARCHAR(120) NOT NULL UNIQUE, mobile CHAR(10) NOT NULL,
  dob DATE, gender ENUM('Male','Female','Other'), location VARCHAR(80),
  qualification VARCHAR(20) NOT NULL, college VARCHAR(120) NOT NULL, university VARCHAR(120),
  passing_year YEAR NOT NULL, percentage DECIMAL(5,2) NOT NULL, backlogs INT DEFAULT 0,
  primary_tech VARCHAR(40) NOT NULL, secondary_skills VARCHAR(200),
  skill_level ENUM('Basic','Intermediate','Advanced') DEFAULT 'Basic',
  preferred_location VARCHAR(80),
  status ENUM('ACTIVE','PLACED','ON_HOLD','INACTIVE') DEFAULT 'ACTIVE'
);
CREATE TABLE jobs (
  job_id INT AUTO_INCREMENT PRIMARY KEY,
  company_id INT NOT NULL, job_code VARCHAR(20) NOT NULL UNIQUE, title VARCHAR(100) NOT NULL,
  openings INT NOT NULL, employment_type ENUM('Full-time','Internship','Contract'), location VARCHAR(80),
  min_package DECIMAL(4,1), max_package DECIMAL(4,1),
  qualifications VARCHAR(100), min_percentage DECIMAL(5,2), min_year YEAR, max_year YEAR,
  max_backlogs INT DEFAULT 0, experience VARCHAR(40), required_tech VARCHAR(40), required_skills VARCHAR(200),
  posted_date DATE, deadline DATE, status ENUM('DRAFT','OPEN','CLOSED') DEFAULT 'DRAFT',
  FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
CREATE TABLE applications (
  application_id INT AUTO_INCREMENT PRIMARY KEY,
  candidate_id INT NOT NULL, job_id INT NOT NULL,
  eligibility ENUM('ELIGIBLE','NOT_ELIGIBLE') , status VARCHAR(30) DEFAULT 'APPLIED',
  applied_on DATE NOT NULL, UNIQUE (candidate_id, job_id),
  FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
  FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);
CREATE TABLE application_history (
  history_id INT AUTO_INCREMENT PRIMARY KEY, application_id INT NOT NULL,
  from_status VARCHAR(30), to_status VARCHAR(30) NOT NULL, remarks VARCHAR(200),
  changed_by INT, changed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (application_id) REFERENCES applications(application_id)
);
CREATE TABLE interviews (
  interview_id INT AUTO_INCREMENT PRIMARY KEY, application_id INT NOT NULL,
  round ENUM('Aptitude','Technical','Managerial','HR') NOT NULL,
  interview_at DATETIME NOT NULL, mode ENUM('Online','Offline','Telephonic') NOT NULL,
  interviewer VARCHAR(80),
  status ENUM('SCHEDULED','COMPLETED','RESCHEDULED','NO_SHOW','CANCELLED') DEFAULT 'SCHEDULED',
  technical_rating TINYINT, communication_rating TINYINT, problem_solving_rating TINYINT, overall_rating TINYINT,
  result ENUM('NEXT_ROUND','SELECTED','REJECTED','ON_HOLD'), remarks VARCHAR(300),
  FOREIGN KEY (application_id) REFERENCES applications(application_id)
);
CREATE TABLE offers (
  offer_id INT AUTO_INCREMENT PRIMARY KEY, application_id INT NOT NULL,
  designation VARCHAR(80) NOT NULL, package_lpa DECIMAL(4,1) NOT NULL,
  offer_date DATE NOT NULL, expected_joining DATE NOT NULL,
  offer_status ENUM('OFFERED','ACCEPTED','REJECTED','EXPIRED','WITHDRAWN') DEFAULT 'OFFERED',
  actual_joining DATE, joining_status ENUM('PENDING','JOINED','NOT_JOINED','DEFERRED','NO_SHOW') DEFAULT 'PENDING',
  FOREIGN KEY (application_id) REFERENCES applications(application_id)
);
