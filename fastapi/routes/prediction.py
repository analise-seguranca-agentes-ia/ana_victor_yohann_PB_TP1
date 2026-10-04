from datetime import UTC, datetime
from random import choice
from typing import Annotated

from database import get_session
from models.prediction import (GetPredictionResponse, PostPredictionRequest,
                               Prediction)
from models.user import User
from security.auth import get_current_user
from sqlmodel import Session, select

from fastapi import APIRouter, Depends, status

prediction_router = APIRouter(prefix="/predict", tags=["prediction"])


user_intentions = [
    "Refund request",
    "Software bug",
    "Network problem",
    "Account access",
]


@prediction_router.post(
    "",
    response_model=GetPredictionResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_user)],
)
async def predict_intention(
    text: PostPredictionRequest,
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    user_intent = Prediction(
        owner_id=current_user.user_id,
        text=text.text,
        intention=choice(user_intentions),
        created_at=datetime.now(UTC),
    )

    session.add(user_intent)
    session.commit()
    session.refresh(user_intent)

    return user_intent


@prediction_router.get(
    "",
    response_model=list[GetPredictionResponse],
    dependencies=[Depends(get_current_user)],
)
async def get_user_predictions(
    session: Annotated[Session, Depends(get_session)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    predictions = session.exec(
        select(Prediction).where(Prediction.owner_id == current_user.user_id)
    )

    return predictions
