const mysql = require('mysql2/promise');
module.exports = mysql.createPool({
  host: 'localhost',
  port: 3306,
  user: 'root',              // your MySQL Workbench username
  password: 'YOUR_PASSWORD', // your MySQL Workbench password
  database: 'careerbridge',
  waitForConnections: true,
  connectionLimit: 10
});
