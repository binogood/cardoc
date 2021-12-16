from abc import ABCMeta, abstractmethod
from typing import Optional

from app.car.models.car import Car
from core.db.session import session


class CarRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_car_trim(self, trim_id: int) -> Optional[Car]:
        pass

    @abstractmethod
    async def get_by_car_id(self, car_id: int) -> Optional[Car]:
        pass

    @abstractmethod
    async def save(self, car: Car) -> Car:
        pass


class CarMySQLRepo(CarRepo):
    async def get_by_car_trim(self, trim_id: int) -> Optional[Car]:
        return session.query(Car).filter(Car.trim_id == trim_id).first()

    async def get_by_car_id(self, car_id: int) -> Optional[Car]:
        return session.query(Car).filter(Car.car_id == car_id).first()

    async def save(self, car: Car) -> Car:
        session.add(car)
        return car


