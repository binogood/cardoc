from pydantic import BaseModel


class CreateCarTireRequest(BaseModel):
    car_id: int
    tire_id: int

    class Config:
        orm_mode = True
        schema_extra = {"example": {"car_id": 1, "tire_id": 1, }}