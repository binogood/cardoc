from typing import Union, NoReturn

from pythondi import inject

from app.tire.models.tire_type import TireType

from app.tire.repository.tire_type import TireTypeRepo
from core.db.transaction import Transaction, Propagation
from core.exceptions.tire import (
    DuplicateTireTypeException,
)


class TireTypeService:
    @inject()
    def __init__(self, tire_type_repo: TireTypeRepo):
        self.tire_type_repo = tire_type_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_tire_type(self, value: str) -> Union[TireType, NoReturn]:
        if await self.tire_type_repo.get_by_tire_type(name=value):
            raise DuplicateTireTypeException

        tire_type = TireType().create(name=value)
        tire_type = await self.tire_type_repo.save(tire_type)
        return tire_type
