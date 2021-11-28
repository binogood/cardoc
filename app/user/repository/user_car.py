from abc import ABCMeta, abstractmethod

from typing import Optional

from app.user.models.user_car import UserCar
from app.user.models.user import User
from app.car.models.car import Car

from cardoc.core.db.session import session


class UserCarRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_user_car(self, name: str, trim_id: int) -> Optional[UserCar]:
        pass

    @abstractmethod
    async def find_by_user_car(self, trimId: str, user_id: int) -> Optional[UserCar]:
        pass

    @abstractmethod
    async def save(self, user_car: UserCar) -> UserCar:
        pass


class UserCarMySQLRepo(UserCarRepo):
    async def get_by_user_car(self, name: str, trim_id: int) -> Optional[UserCar]:
        return session.query(UserCar).filter(
                    User.name == name,
                    Car.trimId == trim_id,
                ).first()

    # async def find_by_user_car(self, trimId: str, user_id: int) -> Optional[UserCar]:
    #     return session.query(UserCar).filter(car_id == )
    #     pass

    async def save(self, user_car: UserCar) -> UserCar:
        session.add(user_car)
        return user_car