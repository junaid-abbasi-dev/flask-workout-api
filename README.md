# Workout API

A backend API for a workout tracking app used by personal trainers. It stores workouts, reusable exercises, and the sets, reps, or duration that connect an exercise to a workout.

This project uses Flask, SQLAlchemy, and Marshmallow.

## Installation

From the project root:

```bash
pipenv install
pipenv shell
```

Database setup comes in a later step:

```bash
export FLASK_APP=server/app.py
flask db upgrade
python server/seed.py
```

## Run

From the project root, with the Pipenv shell active:

```bash
export FLASK_APP=server/app.py
flask run --port 5555
```

The server listens on `http://127.0.0.1:5555`.

## Endpoints

Endpoint list will be added after the routes are built.
