from pydantic import BaseModel


class QuestionsRequest(BaseModel):
    file_name: str


class GetQuestionsResponse(BaseModel):
    question: str
    answer: str
