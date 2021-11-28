from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {"example": {"name": "candycandy", "password": "11223344", }}


class LoginUserRequest(BaseModel):
    name: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {"example": {"name": "candycandy", "password": "11223344", }}