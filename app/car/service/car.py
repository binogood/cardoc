from typing import Union, NoReturn

from pythondi import inject

from app.car.models.car import Car
from app.car.repository.car import CarRepo
from core.db.transaction import Transaction, Propagation
from core.exceptions.car import (
    DuplicateCarTrimException,
)


class CarService:
    @inject()
    def __init__(self, car_repo: CarRepo):
        self.car_repo = car_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_car(self, trim_id: int) -> Union[Car, NoReturn]:
        if await self.car_repo.get_by_car_trim(trim_id=trim_id):
            raise DuplicateCarTrimException

        car = Car().create(trim_id=trim_id)
        car = await self.car_repo.save(car=car)
        return car
