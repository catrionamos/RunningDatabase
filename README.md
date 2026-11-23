# Running Database

**INFO8021 DevOps Strategy and Automation – Final Project**
Student: Catriona O'Sullivan

Running Database is a Flask web application connected to a PostgreSQL database. It helps runners of all levels find a running program that suits their fitness, log their runs and browse running gear.

## Project Status
The project is **complete** and has been submitted. Every new feature was built on its own branch and merged into `main`.

## Features
| Page | Description |
| --- | --- |
| Home / About | Basic web service pages |
| **Feature 1** – Find a Program | Filter the running programs by fitness level |
| **Feature 2** – Shop | Browse running gear from the products table |
| **Feature 3** – Login / Logout | Sign in with a hashed password stored in the users table |
| **Feature 4** – Log a Run | Logged in users save a run and see their run history |

## Tech Stack
- Python 3.12 / Flask 3.1 with Flask-WTF forms
- PostgreSQL 18 with psycopg2
- Werkzeug password hashing
- pytest for automated testing
- GitHub Actions for the CI pipeline
- Docker and Docker Compose for containerisation

## Getting Started
### Run locally
```
venv\Scripts\activate
pip install -r requirements.txt
python initialise_db.py
python populate_db.py
python run.py
```
Then open http://127.0.0.1:5000/ in a browser.

### Run the tests
```
python -m pytest -v
```

### Run with Docker
Create a `.env` file with `DB_USER`, `DB_PASSWORD` and `DATABASE`, then run:
```
docker compose up --build
```

## Project Structure
- `app/` – routes, forms, templates and stylesheet
- `data/` – csv files and `init.sql` for the Docker database
- `tests/` – `conftest.py` and `test_routes.py`
- `.github/workflows/pipeline.yml` – GitHub Actions pipeline
- `Dockerfile` and `docker-compose.yml` – container set up

## Contact
Maintained by Catriona O'Sullivan – [catrionamos](https://github.com/catrionamos)
