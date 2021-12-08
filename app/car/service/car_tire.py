from pythondi import inject

from app.tire.repository.tire import TireRepo
from app.car.repository.car_tire import CarTireRepo
from app.car.repository.car import CarRepo
from app.car.models.car_tire import CarTire
from core.db.transaction import Transaction, Propagation
from core.utiles.token_helper import TokenHelper
from core.exceptions.car import (
    CarNotFoundException,
)
from core.exceptions.tire import (
    TireNotFoundException
)


class CarTireService:
    @inject()
    def __init__(self, car_tire_repo: CarTireRepo, tire_repo: TireRepo, car_repo: CarRepo):
        self.car_tire_repo = car_tire_repo
        self.tire_repo = tire_repo
        self.car_repo = car_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_car_tire(self, token: str, car_id: int, tire_id: int):
        await self._check_value(token=token, car_id=car_id, tire_id=tire_id)

        car_tire = CarTire().create(car_id=car_id, tire_id=tire_id)
        car_tire = await self.car_tire_repo.save(car_tire=car_tire)
        return car_tire

    async def _check_value(self, token:str, car_id: int, tire_id: int):
        TokenHelper.decode(token)
        if await self.tire_repo.get_by_tire_id(tire_id=tire_id):
            raise TireNotFoundException
        if await self.car_repo.get_by_car_id(car_id=car_id):
            raise CarNotFoundException
        # if await self.car_tire_repo.get_by_car_tire(car_id=car_id, tire_id=tire_id):
        #     raise DuplicateCarTireException