# goit-pythonweb-hw-06

## Project Description

This project is a web application that uses SQLAlchemy for database interactions and Faker for generating fake data. It
includes models for groups, students, teachers, subjects, and grades.

## Installation

### Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/mykola-ovchynnik/goit-pythonweb-hw-06.git
    cd goit-pythonweb-hw-06
    ```

2. Install Poetry:
   Follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation) to install Poetry.

3. Install dependencies:
    ```sh
    poetry install
    ```

4. Activate the virtual environment:
    ```sh
    poetry shell
    ```

### Database Setup

1. Run PostgreSQL using Docker:
    ```sh
    docker run --name my_postgres -p 5432:5432 -e POSTGRES_PASSWORD={your_password} -d postgres
    ```

2. Set up the database URL in the `.env` file:
    ```dotenv
    DATABASE_URL='postgresql://postgres:{your_password}@localhost:5432/postgres'
    ```

### Running the Application

1. Apply database migrations:
    ```sh
    alembic upgrade head
    ```

2. Seed the database with fake data:
    ```sh
    python seed.py
    ```
