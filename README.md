# Backend CRUD Application with FastAPI and PostgreSQL

## Overview

This project is a backend application that implements RESTful CRUD operations using **FastAPI** and **PostgreSQL**.

It provides API endpoints to manage personal details, demonstrating how a Python application interacts with a relational database through structured queries and a modular architecture.

This project is part of an ongoing effort to strengthen backend engineering fundamentals and will continue to evolve with additional features and improvements.

---

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- psycopg2
- Uvicorn

---

## Features

- Create, Read, Update, Delete (CRUD) operations
- RESTful API design
- PostgreSQL database integration
- Modular project structure (separation of concerns)
- JSON-based request and response handling
- Interactive API documentation via Swagger UI

---

## Project Structure
project-folder

- main.py # FastAPI entry point
- db.py # Database connection
- config.py # Configuration variables
- personal_details_service.py # Business logic / CRUD operations
- requirements.txt
- README.md


---

## API Endpoints

| Method | Endpoint | Description |
|------|--------|-------------|
| GET | `/personal-details` | Get all records |
| GET | `/personal-details/{id}` | Get a record by ID |
| POST | `/personal-details` | Create a new record |
| PUT | `/personal-details/{id}` | Update a record |
| DELETE | `/personal-details/{id}` | Delete a record |

---

## Getting Started

### 1. Clone the repository

### 2. Create virtual environment

### 3. Install dependencies

### 4. Configure database

Update database credentials in `config.py`:

### 4. Configure database

Update database credentials in `config.py`:

## Future Improvements
- Input validation enhancements
- Authentication and authorization
- Frontend integration (React / Angular / Vue)
- Docker containerization
- Deployment to cloud environment