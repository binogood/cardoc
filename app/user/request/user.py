from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str
    password: str
    is_admin: bool

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "candycandy",
                "password": "11223344",
                "is_admin": 0,
            }
        }


class LoginUserRequest(BaseModel):
    name: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "candycandy",
                "password": "11223344",
            }
        }