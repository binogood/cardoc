from pydantic import BaseModel


class CreateTireRequest(BaseModel):
    value: str
    tire_type_id: int

    class Config:
        orm_mode = True
        schema_extra = {"example": {"value": "245/45R19", "tire_type_id": 1, }}





