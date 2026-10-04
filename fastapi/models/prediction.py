import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict
from sqlmodel import Field, SQLModel

NAMESPACE = uuid.NAMESPACE_DNS
TARGET_NAME = "prediction"


class Prediction(SQLModel, table=True):
    prediction_id: uuid.UUID = Field(
        default_factory=lambda: uuid.uuid5(NAMESPACE, TARGET_NAME), primary_key=True
    )
    owner_id: uuid.UUID = Field(foreign_key="user.user_id", ondelete="CASCADE")
    text: str
    intention: str
    created_at: datetime


class PostPredictionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str


class GetPredictionResponse(BaseModel):
    text: str
    intention: str
