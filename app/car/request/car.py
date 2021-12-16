from pydantic import BaseModel


class CreateCarRequest(BaseModel):
    trim_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "trim_id": 5000,
            }
        }



