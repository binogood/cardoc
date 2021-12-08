from pydantic import BaseModel
from enum import Enum


class CreateTireTypeRequest(str, Enum):
    front: str = "front"
    rear: str = "rear"