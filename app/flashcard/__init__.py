import csv
import os
from typing import Annotated, List

from app.common.dto.user import UserDto
from app.flashcard.dto.get_questions import QuestionsRequest, GetQuestionsResponse
from .constant import FILE_DIRECTORY
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from app.common.auth.jwt import get_current_user
import shutil

flashcard_router = APIRouter(prefix="/api/flashcard")


def get_file(file_name: str):
    return os.path.join(FILE_DIRECTORY, file_name)


def make_file_directory():
    if not os.path.exists(FILE_DIRECTORY):
        os.makedirs(FILE_DIRECTORY)


@flashcard_router.post("/upload_file")
def upload_file(
    file: UploadFile, current_user: Annotated[UserDto, Depends(get_current_user)]
):
    if file.filename is None:
        raise HTTPException(status_code=400, detail="File name is null")

    make_file_directory()
    with open(get_file(file.filename), "wb") as f:
        shutil.copyfileobj(file.file, f)

    return {"result": "success"}


@flashcard_router.post("/get_data")
def get_data(request: QuestionsRequest) -> List[GetQuestionsResponse]:
    try:
        result = []
        with open(get_file(request.file_name)) as f:
            csv_reader = csv.reader(f, delimiter=",")
            for question, answer in csv_reader:
                result.append(GetQuestionsResponse(question=question, answer=answer))
        return result
    except Exception as ex:
        raise HTTPException(500, f"Exception occur {ex}")


@flashcard_router.post("/get_options")
def get_options() -> List[str]:
    make_file_directory()
    try:
        result = []
        for file_name in os.listdir(FILE_DIRECTORY):
            result.append(file_name)
        result.sort()
        return result
    except Exception as ex:
        raise HTTPException(500, f"Exception occur {ex}")


@flashcard_router.post("/delete_option")
def delete_option(
    request: QuestionsRequest,
    current_user: Annotated[UserDto, Depends(get_current_user)],
):
    os.remove(get_file(request.file_name))
    return {"result": "success"}
