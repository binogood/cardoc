
from typing import Union, NoReturn

from pythondi import inject

from app.car.models.car import Car
from app.car.repository.car import CarRepo
from cardoc.core.db.transaction import Transaction, Propagation
from cardoc.core.utiles.token_helper import TokenHelper
from cardoc.core.exceptions.car import (
    DuplicateCarTrimException,
)


class CarService:
    @inject()
    def __init__(self, car_repo: CarRepo):
        self.car_repo = car_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_car(self, token: str, trimId: int) -> Union[Car, NoReturn]:
        TokenHelper.decode(token)
        if await self.car_repo.get_by_car_trim(trimId=trimId):
            raise DuplicateCarTrimException

        car = Car().create(trimId=trimId)
        car = await self.car_repo.save(car=car)
        return car

