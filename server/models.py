# Database models. Exercise, Workout, and WorkoutExercise will be defined here.
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here
class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)

class Workout(db.Model):
    __tablename__ = 'workout'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.Text)