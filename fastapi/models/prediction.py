from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Prediction(BaseModel):
    text: str
    intention: str
    created_at: datetime

    def to_response(self):
        return PredictionResponse(text=self.text, intention=self.intention)


class PredictionCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


class PredictionResponse(BaseModel):
    text: str
    intention: str
