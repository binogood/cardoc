from pydantic import BaseModel


class CreateTireTypeRequest(BaseModel):
    name: str

    class Config:
        orm_mode = True
        schema_extra = {"example": {"name": "front", }}