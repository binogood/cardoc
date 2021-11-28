from pydantic import BaseModel


class CreateTireResponse(BaseModel):
    tire_id: int
    value: str
    tire_type_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "tire_id": 1,
                "value": "245/45R19",
                "tire_type_id": 1,
            }
        }






