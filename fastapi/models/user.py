from pydantic import BaseModel, ConfigDict, EmailStr


class User(BaseModel):
    model_config = ConfigDict(extra="forbid")

    username: str
    email: EmailStr | None = None
    full_name: str | None = None
    hashed_password: str
