from marshmallow import Schema, fields, validates, ValidationError

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str()
    equipment_needed = fields.Bool()

    workouts = fields.Nested(
    lambda: WorkoutSchema(only=("id", "date", "duration_minutes", "notes")),
    many=True,
    dump_only=True,
    )

    @validates("name")
    def validate_name(self, value):
        if not value or not value.strip():
            raise ValidationError("Name must not be empty.")

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(dump_only=True)
    exercise_id = fields.Int(dump_only=True)
    reps = fields.Int(allow_none=True)
    sets = fields.Int(allow_none=True)
    duration_seconds = fields.Int(allow_none=True)

    exercise = fields.Nested(
    ExerciseSchema,
    only=("id", "name", "category", "equipment_needed"),
    dump_only=True,
    )

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str()
    workout_exercises = fields.Nested(WorkoutExerciseSchema, many=True, dump_only=True)

    @validates("duration_minutes")
    def validate_duration_minutes(self, value):
        if value is None or value <= 0:
            raise ValidationError("Duration minutes must be greater than 0.")

