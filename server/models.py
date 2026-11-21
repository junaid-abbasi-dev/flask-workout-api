# Database models. Exercise, Workout, and WorkoutExercise will be defined here.
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
db = SQLAlchemy()

# Define Models here
class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)

    workout_exercises = db.relationship('WorkoutExercise', back_populates='exercise')
    workouts = db.relationship('Workout', secondary='workoutExercise', back_populates='exercises')

    @validates('name')
    def validate_name(self, key, name):
        if not name or not name.strip():
            raise ValueError("Name must not be empty.")
        return name

class Workout(db.Model):
    __tablename__ = 'workout'
    __table_args__ = (
    CheckConstraint('duration_minutes > 0', name='duration_must_be_positive'),
    )

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship('WorkoutExercise', back_populates='workout')
    exercises = db.relationship('Exercise', secondary='workoutExercise', back_populates='workouts')

    @validates('duration_minutes')
    def validate_duration_minutes(self, key, duration_minutes):
        if duration_minutes is None or duration_minutes <= 0:
            raise ValueError("Duration minutes must not be empty or less than 0")
        return duration_minutes

class WorkoutExercise(db.Model):
    __tablename__ = 'workoutExercise'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

