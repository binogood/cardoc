from pydantic import BaseModel


class CreateCarResponse(BaseModel):
    car_id: int
    trim_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "car_id": 1,
                "trim_id": 5000,
            }
        }

