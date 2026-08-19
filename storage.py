import json
import os

FILE_PATH = "data/students.json"

def load_students():
    """load students data from the json file"""
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    

def save_students(students):
    """save studnets data to the json file"""
    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=3)