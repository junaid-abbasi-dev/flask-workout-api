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
cd server
python seed.py
```

## Run

From the project root, with the Pipenv shell active:

```bash
export FLASK_APP=server/app.py
flask run --port 5555
```

The server listens on `http://127.0.0.1:5555`.

## Endpoints
## Endpoints

- `GET /workouts` lists every workout, including each exercise with reps, sets, and duration.
- `GET /workouts/<id>` returns one workout. A missing id returns 404.
- `POST /workouts` creates a workout. Send JSON with `date`, `duration_minutes`, and optional `notes`. Success returns 201. A bad duration returns 400.
- `DELETE /workouts/<id>` deletes that workout and its exercise links.
- `GET /exercises` lists every exercise, including the workouts that use it.
- `GET /exercises/<id>` returns one exercise. A missing id returns 404.
- `POST /exercises` creates an exercise. Send JSON with `name`, `category`, and `equipment_needed`. A blank name returns 400.
- `DELETE /exercises/<id>` deletes that exercise and its workout links.
- `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` adds an exercise to a workout. Send JSON with `reps`, `sets`, and `duration_seconds`. Any of those numbers can be null.
Endpoint list will be added after the routes are built.
