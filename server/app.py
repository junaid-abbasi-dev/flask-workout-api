# Flask application entry point. Routes will be added in a later step.
from flask import Flask, make_response, request
from marshmallow import ValidationError
from flask_migrate import Migrate
from schemas import WorkoutSchema, ExerciseSchema
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
workouts_schema = WorkoutSchema(many=True)
workout_schema = WorkoutSchema()
exercises_schema = ExerciseSchema(many=True)

# Define Routes here
@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return make_response(workouts_schema.dump(workouts)), 200

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if workout is None:
        return make_response({"error": "Workout not found"}, 404)
    return make_response(workout_schema.dump(workout), 200)

@app.route('/workouts', methods=['POST'])
def create_workout():
    try:
        data = workout_schema.load(request.get_json())
    except ValidationError as err:
        return make_response({"errors": err.messages}, 400)

    workout = Workout(**data)
    db.session.add(workout)
    db.session.commit()
    return make_response(workout_schema.dump(workout), 201)

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if workout is None:
        return make_response({"error": "Workout not found"}, 404)
    for link in workout.workout_exercises:
        db.session.delete(link)
    db.session.delete(workout)
    db.session.commit()
    return make_response({"message": "Workout deleted"}, 200)

@app.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return make_response(exercises_schema.dump(exercises), 200)

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    return make_response({"message": "One exercise"}, 200)

@app.route('/exercises', methods=['POST'])
def create_exercise():
    return make_response({"message": "Exercise created"}, 201)

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    return make_response({"message": "Exercise deleted"}, 200)

@app.route('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
    return make_response({"message": "Exercise added to workout"}, 201)
if __name__ == '__main__':
    app.run(port=5555, debug=True)
