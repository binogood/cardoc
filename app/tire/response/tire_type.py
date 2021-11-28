from pydantic import BaseModel


class CreateTireTypeResponse(BaseModel):
    tire_type_id: int
    name: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "tire_type_id": 1,
                "name": "front",
            }
        }