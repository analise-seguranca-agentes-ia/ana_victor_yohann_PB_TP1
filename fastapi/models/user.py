from datetime import datetime

from pydantic import BaseModel, EmailStr


class Prediction(BaseModel):
    text: str
    intention: str
    created_at: datetime

    def to_response(self):
        return PredictionResponse(text=self.text, intention=self.intention)


class PredictionCreate(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    text: str
    intention: str


class User(BaseModel):
    username: str
    email: EmailStr | None = None
    full_name: str | None = None
    hashed_password: str
