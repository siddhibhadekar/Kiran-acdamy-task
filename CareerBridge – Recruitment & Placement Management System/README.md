# CareerBridge – Recruitment & Placement Management System (RPMS)

A web-based system for managing the complete campus recruitment and placement cycle: candidates, companies, job openings, applications, interviews, offers and joining, with reports.

Developed as a project at **Kiran Academy**.

> **Status:** Front-end prototype screens with sample data, plus a Node.js + MySQL back-end starter. Nothing is saved from the static forms until they are wired to the API.

---

## Features

| Module | What it does |
|---|---|
| **Login** | Role-based login screen (Admin, Recruiter, Placement Officer) |
| **Dashboard** | Totals, recruitment funnel, upcoming interviews, recent jobs and placements |
| **Candidates** | Search, filter, add, edit and view profiles (academic details, skills, history) |
| **Companies** | Add and edit companies, HR contacts, open jobs count |
| **Jobs** | Create and edit jobs with package, eligibility criteria, skills and deadlines |
| **Applications** | Track applications, check eligibility, shortlist, reject, view status history |
| **Interviews** | Schedule, reschedule, mark no-show, record ratings and results |
| **Placement Process** | Interview feedback → offer details → joining / placed |
| **Reports** | Funnel, company-wise and technology-wise placement, recruiter performance, job aging |

## Placement workflow

`Applied → Eligible → Shortlisted → Interview → Selected → Offered → Joined → Placed`

## Tech stack

- **Front end:** HTML5, CSS3 (shared `css/style.css`, violet theme, responsive)
- **Back end:** Node.js, Express
- **Database:** MySQL 8 (MySQL Workbench)
- **DB driver:** `mysql2`

## Project structure

```
CareerBridge/
├── login.html
├── dashboard.html
├── candidates.html
├── candidate-form.html
├── candidate-details.html
├── companies.html
├── jobs.html
├── job-form.html
├── applications.html
├── interviews.html
├── placement-process.html
├── reports.html
├── css/
│   └── style.css
├── images/
│   └── logo.svg
├── database/
│   └── schema.sql
├── server/
│   ├── package.json
│   ├── db.js
│   └── server.js
└── README.md
```

## Getting started

### Prerequisites
- [Node.js](https://nodejs.org) 18 or later
- MySQL Server 8 and MySQL Workbench

### 1. Set up the database
1. Open **MySQL Workbench** and connect to your local server (`127.0.0.1`, port `3306`, user `root`).
2. Choose **File → Open SQL Script**, select `database/schema.sql` and click the ⚡ **Run** button.
3. Refresh the Schemas panel. You should see the `careerbridge` database.

### 2. Configure the connection
Edit `server/db.js`:

```js
host: 'localhost',
user: 'root',
password: 'YOUR_PASSWORD',
database: 'careerbridge'
```

### 3. Run the server
```bash
cd server
npm install
npm start
```

### 4. Open the app
- Connection test: <http://localhost:3000/api/test>
- Application: <http://localhost:3000/login.html>

To preview only the screens (no database), open `login.html` directly in a browser.

## Database tables

`users`, `companies`, `candidates`, `jobs`, `applications`, `application_history`, `interviews`, `offers`

Key rules built into the schema:
- A candidate can apply to a job only once (`UNIQUE (candidate_id, job_id)`).
- Candidate email and job code are unique.
- Every status change is stored in `application_history`.

## API (starter)

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/test` | Checks the MySQL connection |
| GET | `/api/candidates` | List all candidates |
| POST | `/api/candidates` | Add a candidate |

More endpoints (companies, jobs, applications, interviews, offers, reports) follow the same pattern in `server/server.js`.

## Validation rules (shown in the forms)

- Mobile number must be 10 digits.
- Percentage must be between 0 and 100.
- Email must be valid and unique.
- Number of openings must be greater than zero.
- Minimum package cannot exceed maximum package.
- Application deadline cannot be before the posted date.
- Interview date cannot be in the past.
- A candidate cannot apply twice for the same job.

## Roadmap

- [ ] Connect every page to the API (replace sample data)
- [ ] Password hashing and session / JWT login
- [ ] Automatic eligibility check on application
- [ ] Export reports to PDF / Excel
- [ ] Email notifications for interviews and offers

## Author

**Shivam Raut** – Kiran Academy Tasks
