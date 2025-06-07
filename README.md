# Student Management System

A simple web application to manage student records using Flask (Python) backend and MySQL database, with a modern and responsive frontend.

---

## Features

- Add new students with ID, Name, Department, and Year.
- View all students in a styled table.
- Update existing student details.
- Delete students by ID.
- RESTful API endpoints for all CRUD operations.
- Frontend communicates with backend via Fetch API.
- CORS enabled for cross-origin requests.

---

## Tech Stack

- Backend: Flask (Python)
- Database: MySQL
- Frontend: HTML, CSS, JavaScript (Fetch API)
- Flask-CORS for handling cross-origin requests
- flask-mysqldb for MySQL integration

---

## Setup Instructions

### Prerequisites

- Python 3.x installed
- MySQL installed and running
- `pip` package manager installed

### Backend Setup

1. Clone the repository or copy the project files.

2. Create a MySQL database named `campus_drive`.

3. Create the `students` table using this SQL query:

   ```sql
   CREATE TABLE students (
       id INT PRIMARY KEY,
       name VARCHAR(100),
       department VARCHAR(100),
       year INT
   );

Install required Python packages:
pip install flask flask-mysqldb flask-cors


Update MySQL credentials in app.py:
```sql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'campus_drive'
```
Run the Flask app:
```python
python app.py
```
The server will start on http://localhost:5000
