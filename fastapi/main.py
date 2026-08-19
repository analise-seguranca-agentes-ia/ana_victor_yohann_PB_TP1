import uvicorn
from routes import auth, health, prediction

from fastapi import FastAPI

app = FastAPI()

app.include_router(auth.router)
app.include_router(health.router)
app.include_router(prediction.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
