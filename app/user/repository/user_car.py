from abc import ABCMeta, abstractmethod
from typing import Optional

from app.user.models.user_car import UserCar

from core.db.session import session


class UserCarRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_user_car(self, car_id: int, user_id: int) -> Optional[UserCar]:
        pass

    @abstractmethod
    async def save(self, user_car: UserCar) -> UserCar:
        pass


class UserCarMySQLRepo(UserCarRepo):
    async def get_by_user_car(self, car_id: int, user_id: int) -> Optional[UserCar]:
        return session.query(UserCar).filter(
                    UserCar.user_id == user_id,
                    UserCar.car_id == car_id
                ).first()

    async def save(self, user_car: UserCar) -> UserCar:
        session.add(user_car)
        return user_car