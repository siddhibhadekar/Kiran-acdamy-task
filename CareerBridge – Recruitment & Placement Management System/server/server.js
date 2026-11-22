const express = require('express');
const cors = require('cors');
const path = require('path');
const db = require('./db');
const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '..'))); // serves the HTML pages

app.get('/api/test', async (req, res) => {
  try { const [r] = await db.query('SELECT 1 AS ok'); res.json({ connected: true, r }); }
  catch (e) { res.status(500).json({ connected: false, error: e.message }); }
});
app.get('/api/candidates', async (req, res) => {
  const [rows] = await db.query('SELECT * FROM candidates');
  res.json(rows);
});
app.post('/api/candidates', async (req, res) => {
  const c = req.body;
  const [r] = await db.query(
    `INSERT INTO candidates (full_name,email,mobile,qualification,college,passing_year,percentage,backlogs,primary_tech)
     VALUES (?,?,?,?,?,?,?,?,?)`,
    [c.full_name,c.email,c.mobile,c.qualification,c.college,c.passing_year,c.percentage,c.backlogs,c.primary_tech]);
  res.json({ id: r.insertId });
});
app.listen(3000, () => console.log('Open http://localhost:3000/login.html'));
