"""
To run (after environment setup):
(env) $ python -m pip install -r requirements.txt
(env) $ FLASK_DEBUG=True python -m flask run
"""

import csv
from flask import Flask, request, Response
import repos.utils as utils
from repos.constants import CSV_FILE, CSV_FIELDS


app = Flask(__name__)


@app.route('/user')
def get_users():
    return utils.read_users()


@app.route("/user/<user_id>")
def get_user(user_id):
    users = utils.read_users()
    user = next((item for item in users if item['id'] == user_id), None)

    if user is None:
        return Response("User not found", status=404)

    return user


@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or not "name" in data or not "surname" in data or not "age" in data:
        return Response("Invalid data", status=400)

    user_name = data["name"]
    user_surname = data["surname"]
    user_age = data["age"]

    users = utils.read_users()
    if users and users[-1]["id"]:
        user_id = int(users[-1]["id"]) + 1
    else:
        user_id = 1

    try:
        with open(CSV_FILE, "a") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)

            if user_id == 1:
                writer.writeheader()

            writer.writerow({
                "id": user_id,
                "name": user_name,
                "surname": user_surname,
                "age": user_age
            })
        return Response("User created", status=201)
    except Exception as error:
        return Response(f"Error: {error}", status=500)


@app.route("/user", methods=["PUT"])
def update_user():
    return "Update User"


@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return f"Delete user with ID: {user_id}"
