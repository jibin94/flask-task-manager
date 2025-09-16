# ✅ Task Manager (Flask + SQLAlchemy)

A simple **Task Manager** web app and REST API built with **Flask**, **SQLAlchemy**, and Bootstrap.  
It supports creating, reading, updating & deleting tasks (CRUD).


## Project Structure

taskmanager/
│
├── app/
│   ├── __init__.py          # App factory, DB init, blueprints
│   ├── extensions.py        # SQLAlchemy instance
│   ├── models.py           # Database models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── api_routes.py   # REST API routes
│   │   └── html_routes.py  # Web interface routes
│   └── templates/
│       ├── index.html
│       └── update.html
│
├── migrations/             # (Optional) Flask-Migrate files
├── README.md
└── run.py                 # App entry point

## Features

- Web interface for managing tasks  
- RESTful API for programmatic access  
- SQLite database (can switch to PostgreSQL/MySQL)  
- Clean architecture with Blueprints & App Factory

## Create & activate a virtual environment (MacOS)
```
python3 -m venv .venv
source .venv/bin/activate
```

## Running the App

Start the server:
```
python3 run.py
```
Then open your browser: http://127.0.0.1:5000

## API Endpoints

| Method | Endpoint          | Description       | Body (JSON)                                     |
| ------ | ----------------- | ----------------- | ----------------------------------------------- |
| GET    | `/api/tasks`      | Get all tasks     | –                                               |
| POST   | `/api/tasks`      | Create a new task | `{ "content": "Buy fruits", "is_done": false }` |
| GET    | `/api/tasks/<id>` | Get a single task | –                                               |
| PUT    | `/api/tasks/<id>` | Update task       | `{ "content": "Buy fruits", "is_done": true }`  |
| DELETE | `/api/tasks/<id>` | Delete task       | –                                               |


