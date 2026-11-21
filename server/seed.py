#!/usr/bin/env python3

# Resets the database and inserts example workouts and exercises.
from app import app
from models import *

with app.app_context():

	# reset data and add new example data, committing to db
