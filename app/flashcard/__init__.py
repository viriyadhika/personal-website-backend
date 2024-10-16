import csv
import os
from typing import List
from flask import Blueprint, abort, make_response, request
from flask_jwt_extended import jwt_required
from .constant import FILE_DIRECTORY

flashcard_blueprint: Blueprint = Blueprint(
    "flashcard", __name__, url_prefix="/api/flashcard"
)


def get_file(file_name: str):
    return os.path.join(FILE_DIRECTORY, file_name)


def make_file_directory():
    if not os.path.exists(FILE_DIRECTORY):
        os.makedirs(FILE_DIRECTORY)


@flashcard_blueprint.route("/upload_file", methods=["POST"])
@jwt_required()
def upload_file():
    make_file_directory()
    f = request.files.get("file")
    f.save(get_file(f.filename))

    return {"result": "success"}


@flashcard_blueprint.route("/get_data", methods=["POST"])
def get_data():
    try:
        file_name = request.get_json()["file_name"]
        result = []
        with open(get_file(file_name)) as f:
            csv_reader = csv.reader(f, delimiter=",")
            for question, answer in csv_reader:
                result.append({"question": question, "answer": answer})
        return result
    except Exception as ex:
        abort(make_response({"message": f"Exception occur {ex}"}, 500))


@flashcard_blueprint.route("/get_options", methods=["POST"])
def get_options() -> List[str]:
    make_file_directory()
    try:
        result = []
        for file_name in os.listdir(FILE_DIRECTORY):
            result.append(file_name)
        result.sort()
        return result
    except Exception as ex:
        abort(make_response({"message": f"Exception occur {ex}"}, 500))


@flashcard_blueprint.route("/delete_option", methods=["POST"])
@jwt_required()
def delete_option():
    file_name = request.get_json()["file_name"]
    os.remove(get_file(file_name))
    return {"result": "success"}
