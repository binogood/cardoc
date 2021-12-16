from typing import Union, NoReturn
from fastapi import Request
from pythondi import inject

from app.user.models.user_car import UserCar
from app.user.repository.user import UserRepo
from app.car.repository.car import CarRepo
from app.car.repository.car_tire import CarTireRepo
from app.user.repository.user_car import UserCarRepo
from core.db.transaction import Transaction, Propagation
from core.exceptions.user import (
    DuplicateUserCarException,
    ManyRequestsException,
)
from core.exceptions.car import (
    CarNotFoundException
)


class UserCarService:
    @inject()
    def __init__(self,
                 user_car_repo: UserCarRepo,
                 user_repo: UserRepo,
                 car_repo: CarRepo,
                 car_tire_repo: CarTireRepo,
        ):
        self.user_car_repo = user_car_repo
        self.user_repo = user_repo
        self.car_repo = car_repo
        self.car_tire_repo = car_tire_repo

    @Transaction(propagation=Propagation.REQUIRED)
    async def create_user_car(
                    self,
                    user_info: Request,
                    user_car_info: list,
                ) -> Union[UserCar, NoReturn]:
        user_id = user_info.user.id
        if len(user_car_info) > 5:
            raise ManyRequestsException
        user_car_list = []
        for value in user_car_info:
            value = value.dict()
            car_id = await self._check_value(value, user_id)

            user_car = UserCar().create(car_id=car_id, user_id=user_id)
            user_car = await self.user_car_repo.save(user_car=user_car)
            user_car_list.append(user_car)

        return user_car_list

    @Transaction(propagation=Propagation.REQUIRED)
    async def get_user_car(self, trim_id: int, name: str) -> Union[UserCar, NoReturn]:
        return await self._user_car_info(trim_id=trim_id, name=name)

    async def _user_car_info(self, trim_id: int, name: str) -> dict:
        user = await self.user_repo.get_by_name(name=name)
        car = await self.car_repo.get_by_car_trim(trim_id=trim_id)
        car_tire = await self.car_tire_repo.get_by_car_tire_info(car_id=car.car_id)
        car_tire_info = {'id': user.name, "trim_id": car.trim_id, "car_tire": car_tire}
        return car_tire_info

    async def _check_value(self, value: dict, user_id: int) -> int:
        car = await self.car_repo.get_by_car_trim(trim_id=value['trim_id'])
        if not car:
            raise CarNotFoundException
        if await self.user_car_repo.get_by_user_car(car_id=car.car_id, user_id=user_id):
            raise DuplicateUserCarException

        return car.car_id