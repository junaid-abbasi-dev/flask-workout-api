#!/usr/bin/env python3

# Resets the database and inserts example workouts and exercises.
from app import app
from models import *
from datetime import date

with app.app_context():

	WorkoutExercise.query.delete()
	Workout.query.delete()
	Exercise.query.delete()
	db.session.commit()

	pushup = Exercise(name="Push-up", category="strength", equipment_needed=False)
	squat = Exercise(name="Squat", category="strength", equipment_needed=False)
	plank = Exercise(name="Plank", category="core", equipment_needed=False)

	db.session.add_all([pushup, squat, plank])
	db.session.commit()

	leg_day = Workout(date=date(2026, 11, 20), duration_minutes=45, notes="Felt strong")
	upper_body = Workout(date=date(2026, 11, 19), duration_minutes=40, notes="Felt energetic")

	db.session.add_all([leg_day, upper_body])
	db.session.commit()

	leg_squat = WorkoutExercise(workout=leg_day, exercise=squat, reps=10, sets=3, duration_seconds=None)
	upper_pushup = WorkoutExercise(workout=upper_body, exercise=pushup, reps=12, sets=3, duration_seconds=None)
	upper_plank = WorkoutExercise(workout=upper_body, exercise=plank, reps=None, sets=3, duration_seconds=60)

	db.session.add_all([leg_squat, upper_pushup, upper_plank])
	db.session.commit()