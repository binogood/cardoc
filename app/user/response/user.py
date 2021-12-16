from datetime import datetime
from pydantic import BaseModel


class CreateUserResponse(BaseModel):
    user_id: int
    name: str
    password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "user_id": 1,
                "name": "candycandy",
                "password": "11223344",
                "created_at": "2021-11-11T07:50:54.289Z",
                "updated_at": "2021-11-11T07:50:54.289Z",
            }
        }


class LoginUserResponse(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "access_token": "token",
                "token_type": "bearer",
            }
        }