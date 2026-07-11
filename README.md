# Student Frontend - Week 2

## Project Description
This project is a Student Management System frontend built using Flask, HTML, CSS, and JavaScript. The frontend communicates with a Flask REST API to perform CRUD (Create, Read, Update, Delete) operations on student records.

## Features
- Add Student
- View Students
- Edit Student
- Delete Student
- Loading message
- Error handling

## Technologies Used
- Python
- Flask
- HTML5
- CSS3
- JavaScript
- SQLite

## Project Structure

```
Student-Frontend-Week2
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the application

```bash
python app.py
```

### 3. Open in browser

```
http://127.0.0.1:5000/home
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /students | Get all students |
| GET | /students/<id> | Get a student |
| POST | /students | Add a student |
| PUT | /students/<id> | Update a student |
| DELETE | /students/<id> | Delete a student |

## Week 2 Task Completed

✔ Frontend consuming Flask REST API

✔ Add Student

✔ View Students

✔ Edit Student

✔ Delete Student

✔ Loading and Error Messages

✔ Responsive UI
