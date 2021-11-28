
from pydantic import BaseModel


class CreateCarResponse(BaseModel):
    car_id: int
    trimId: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "car_id": 1,
                "trimId": 5000,
            }
        }

