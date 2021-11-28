from pydantic import BaseModel


class CreateCarRequest(BaseModel):
    trimId: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "trimId": 5000,
            }
        }



