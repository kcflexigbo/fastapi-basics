# Database Setup Project

A FastAPI-based web application for managing users and books with PostgreSQL database integration.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Database Setup](#database-setup)
- [Database Migrations](#database-migrations)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [License](#license)

## Overview

This project provides a RESTful API for managing users and books in a library system. It uses FastAPI for the web framework, PostgreSQL as the database, and SQLAlchemy as the ORM. The project also includes Alembic for database migrations.

## Features

- User management (create users with roles)
- Book management (create books, assign books to users)
- PostgreSQL database integration
- Database migration support with Alembic
- RESTful API design
- CORS support

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs with Python 3.7+
- [PostgreSQL](https://www.postgresql.org/) - Powerful, open source object-relational database system
- [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL toolkit and Object Relational Mapper
- [Alembic](https://alembic.sqlalchemy.org/) - Lightweight database migration tool for SQLAlchemy
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and settings management using Python type annotations

## Project Structure

```
.
├── alembic/                 # Database migration files
│   ├── versions/            # Migration scripts
│   └── env.py               # Alembic configuration
├── api/                     # API route definitions
│   ├── book.py              # Book-related endpoints
│   └── user.py              # User-related endpoints
├── crud/                    # CRUD operations
│   ├── crud_book.py         # Book CRUD operations
│   └── crud_user.py         # User CRUD operations
├── alembic.ini              # Alembic configuration file
├── database.py              # Database connection setup
├── main.py                  # Application entry point
├── models.py                # Database models
├── schemas.py               # Pydantic schemas for request/response validation
└── readme.md                # This file
```

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7 or higher
- PostgreSQL database server
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd database-setup
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy alembic psycopg2-binary python-dotenv
   ```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASS=your_database_password
```

## Database Setup

Before running migrations, you need to create the PostgreSQL database:

1. Connect to PostgreSQL:
   ```bash
   psql -U postgres
   ```

2. Create the database:
   ```sql
   CREATE DATABASE your_database_name;
   ```

3. You can also create a dedicated user for the application:
   ```sql
   CREATE USER your_database_user WITH PASSWORD 'your_database_password';
   GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_database_user;
   ```

Alternatively, you can use a database management tool like pgAdmin to create the database.

Note: The current migration system does not automatically create the database if it doesn't exist. Alembic only manages the schema within an existing database. You must manually create the database first before running migrations.

## Database Migrations

This project uses Alembic for database migrations:

- To generate a new migration:
  ```bash
  alembic revision --autogenerate -m "Migration message"
  ```

- To apply migrations:
  ```bash
  alembic upgrade head
  ```

- To downgrade migrations:
  ```bash
  alembic downgrade -1
  ```

## API Endpoints

### User Endpoints

- `POST /user/create_user` - Create a new user
- `GET /user/{username}` - Retrieve a user by username

### Book Endpoints

- `POST /book/create_book` - Create a new book
- `POST /book/{user_id}/assign` - Assign a book to a user
- `GET /book/{book_serial_number}` - Retrieve a book by serial number

### Root Endpoint

- `GET /root` - Root endpoint returning "Hello World"

## Usage

After starting the server, you can access:

1. The API documentation at `http://localhost:8000/docs`
2. The alternative API documentation at `http://localhost:8000/redoc`

To start the server:
```bash
uvicorn main:app --reload
```

## License

This project is licensed under the MIT License.