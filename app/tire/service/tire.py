
from typing import Union, NoReturn

from pythondi import inject

from app.tire.models.tire import Tire

from app.tire.repository.tire import TireRepo
from core.db.transaction import Transaction, Propagation
from core.exceptions.tire import (
    DuplicateTireException,
)


class TireService:
    @inject()
    def __init__(self, tire_repo: TireRepo):
        self.tire_repo = tire_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_tire(self, value: str, tire_type_id: int) -> Union[Tire, NoReturn]:
        if await self.tire_repo.get_by_tire(value=value, tire_type_id=tire_type_id):
            raise DuplicateTireException

        tire = Tire().create(value=value, tire_type_id=tire_type_id)
        tire = await self.tire_repo.save(tire=tire)
        return tire


