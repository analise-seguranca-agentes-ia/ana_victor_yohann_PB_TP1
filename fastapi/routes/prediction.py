from datetime import datetime
from random import choice

from models.user import Prediction, PredictionCreate, PredictionResponse
from security.auth import get_current_user

from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/predict", tags=["prediction"])


user_intentions = [
    "Refund request",
    "Software bug",
    "Network problem",
    "Account access",
]


@router.post(
    "/",
    response_model=PredictionResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_current_user)],
)
async def predict_intention(text: PredictionCreate):
    user_intention = Prediction(
        text=text.text,
        intention=choice(user_intentions),
        created_at=datetime.now(),
    )

    return user_intention
