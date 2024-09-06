import csv
import os
from flask import Blueprint, abort, make_response, request
from flask_jwt_extended import jwt_required
from .constant import FILE_DIRECTORY, FILE_NAME

flashcard_blueprint: Blueprint = Blueprint(
    "flashcard", __name__, url_prefix="/api/flashcard"
)


def get_file():
    return os.path.join(FILE_DIRECTORY, FILE_NAME)


@flashcard_blueprint.route("/upload_file", methods=["POST"])
@jwt_required()
def upload_file():
    if request.method == "POST":
        # upload file flask
        if not os.path.exists(FILE_DIRECTORY):
            os.makedirs(FILE_DIRECTORY)

        f = request.files.get("file")
        f.save(get_file())

        return {"result": "success"}


@flashcard_blueprint.route("/get_data", methods=["POST"])
def get_data():
    if request.method == "POST":
        try:
            with open(get_file()) as f:
                result = []
                csv_reader = csv.reader(f, delimiter=",")
                for question, answer in csv_reader:
                    result.append({"question": question, "answer": answer})

                return result
        except Exception as ex:
            return abort(make_response({"message": f"Exception occur {ex}"}, 500))
