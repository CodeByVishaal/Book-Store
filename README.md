# Book Store Web Application

Welcome to the **Book Catalog Web Application**!  
This project is a **Flask-based web application** designed for managing a catalog of books.  
It provides a clean and intuitive interface for adding, viewing, and editing book entries.  
The application also includes basic user management features.

## Features
- **Book Management**: Add, view, and update book details.
- **User Management**: Creates a default user on initial setup.
- **Flask and SQLAlchemy Integration**: Uses Flask for web framework and SQLAlchemy for database operations.

## Getting Started

### Prerequisites
Before you begin, ensure you have the following installed:
- **Python 3.x**: Python programming language.
- **Flask**: Web framework for Python.
- **Flask-SQLAlchemy**: SQLAlchemy extension for Flask.

### Installation

#### Clone the Repository
```bash
git clone https://github.com/Vishaalcodre/Book-Store.git
```

#### Navigate to the Project Directory
```bash
cd book-store
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

### Running the Application

#### Start the Flask Application
```bash
python run.py
```

#### Access the Application
Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to start using the Book Catalog.

## Code Overview
The core functionality is implemented in `run.py`, which:
- Initializes the Flask application with a production configuration.
- Creates and sets up the database schema using SQLAlchemy.
- Ensures a default user exists in the database, creating one if necessary.
- Launches the Flask server for development.

### Code Structure
```
app/                 # Main application package
  __init__.py        # Sets up the Flask application
  models.py          # Defines the Book and User models

auth/                # Handles authentication and user-related functionalities
  __init__.py        # Initializes the authentication module
  models.py          # Defines the User model

requirements.txt     # Lists the Python packages required for the project
run.py               # The entry point for running the Flask application
```

## Database
The application uses **PostgreSQL** as database and **SQLAlchemy** for ORM-based database operations.  
The database schema and models are defined in `app/models.py`, which includes definitions for book and user entities.

## Contributing
Contributions are welcome! If you want to contribute to the project:
1. **Fork the Repository**: Create your own copy of the project.
2. **Create a Feature Branch**: Develop your feature or fix in a new branch.
3. **Submit a Pull Request**: Share your changes and explain what you’ve done.

## Authors
- Vishal R

## Acknowledgments
- **Flask**: A micro web framework for Python.
- **Flask-SQLAlchemy**: An extension for SQLAlchemy integration with Flask.
- **Inspiration Source**: This project is inspired by the Flask Book Catalog project.

## Changelog
- **v1.0**: Initial release with basic features for book and user management.
