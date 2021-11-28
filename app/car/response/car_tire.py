from pydantic import BaseModel


class CreateCarTireResponse(BaseModel):
    car_tire_id: int
    car_id: int
    tire_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "car_tire_id": 1,
                "car_id": 1,
                "tire_id": 1,
            }
        }