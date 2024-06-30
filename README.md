# Flask Application with SQLAlchemy and CRUD Functionality

## Project Description

This project is a Flask web application that demonstrates basic CRUD (Create, Read, Update, Delete) operations using SQLAlchemy ORM. The application manages three main entities: Groups, Students, and Lessons, with appropriate relationships between them.

## Project Structure

```plaintext
flask_app/
│
├── app.py
├── routes.py
├── templates/
│   ├── base.html
│   ├── group/
│   │   └── management.html
│   ├── student/
│   │   └── management.html
│   └── lesson/
│       └── management.html
├── static/
│   └── (optional: add CSS/JS files here)
├── models/
│   ├── __init__.py
│   ├── database.py
│   └── models.py
└── __init__.py
```

## Installation

1. **Clone the repository:**

```sh
git clone https://github.com/your-username/flask_app.git
cd flask_app
```

2. **Create and activate a virtual environment:**

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install dependencies:**

```sh
pip install -r requirements.txt
```

4. **Set up the database:**

The database is automatically created when you first run the application. Ensure you have SQLite installed, or modify the `DATABASE_URI` in `models/database.py` to point to another SQLAlchemy-supported database.

## Running the Application

1. **Set the FLASK_APP environment variable:**

```sh
export FLASK_APP=app.py  # On Windows, use `set FLASK_APP=app.py`
```

2. **Run the Flask application:**

```sh
flask run
```

The application will be available at `http://127.0.0.1:5000`.

## Features

### Group Management

- View all groups
- Add a new group
- View students in a group

### Student Management

- View all students
- Add a new student to a group
- Manage group associations for students

### Lesson Management

- View all lessons
- Add a new lesson
- Manage group associations for lessons

## Template Structure

### `templates/base.html`

The base template containing the basic structure of the HTML page, including the header and footer.

### `templates/group/management.html`

Template for managing groups, including listing all groups and adding a new group.

### `templates/student/management.html`

Template for managing students, including listing all students and adding a new student.

### `templates/lesson/management.html`

Template for managing lessons, including listing all lessons and adding a new lesson.

## Models

### `models/models.py`

Contains the SQLAlchemy models:

- `Student`
- `Group`
- `Lesson`

### `models/database.py`

Contains the database setup, including session management and functions to create and drop the database.

## Routes

### `routes.py`

Contains the route definitions for:

- Home page
- Group management (view, add)
- Student management (view, add)
- Lesson management (view, add)

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. 

This README.md file provides a comprehensive overview of the Flask application, including project structure, installation instructions, features, and usage. It ensures that anyone who wants to use or contribute to the project has all the necessary information.

Happy coding! 🖥️📡