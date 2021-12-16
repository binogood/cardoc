from pydantic import BaseModel
from typing import Optional, List


class CreateUserCarDetailResponse(BaseModel):
    name: str
    trim_id: int


class CreateUserCarResponse(BaseModel):
    user_car_list: Optional[List[CreateUserCarDetailResponse]]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "user_car_list": [
                    {
                        "name": "candycandy",
                        "trim_id": 5000,
                    },
                ]
            }
        }


class GetTireInfoResponse(BaseModel):
    front: str
    rear: str


class GetUserCarResponse(BaseModel):
    id: str
    trimId: int
    car_tire: Optional[GetTireInfoResponse]

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "id": "candycandy",
                "trim_id": "5000",
                "car_tire" : {
                    "front": "245/45R19",
                    "rear": "245/45R20",
                }

            }
        }