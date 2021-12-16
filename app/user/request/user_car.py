from pydantic import BaseModel
from typing import Optional, List


class CreateUserCarDetailRequest(BaseModel):
    name: str
    trim_id: int


class CreateUserCarRequest(BaseModel):
    user_car_info: Optional[List[CreateUserCarDetailRequest]]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "user_car_info": [
                    {
                        "name": "candycandy",
                        "trim_id": 5000,
                    },
                ]
            }
        }


class GetUserCarRequest(BaseModel):
    trimId: int
    name: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "trim_id": "5000",
                "name": "candycandy",
            }
        }