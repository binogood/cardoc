from abc import ABCMeta, abstractmethod
from typing import Optional

from app.car.models.car_tire import CarTire
from app.tire.models.tire import Tire
from core.db.session import session
from app.tire.enums.tiretype import TireTypeEnum


class CarTireRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_car_tire(self, car_id: int, tire_id: int) -> Optional[CarTire]:
        pass

    async def get_by_car_tire_info(self, car_id: int):
        pass

    @abstractmethod
    async def save(self, car_tire: CarTire) -> CarTire:
        pass


class CarTireMySQLRepo(CarTireRepo):
    async def get_by_car_tire(self, car_id: int, tire_id: int) -> Optional[CarTire]:
        return session.query(CarTire).filter(
                    CarTire.car_id == car_id,
                    CarTire.tire_id == tire_id,
                ).first()

    async def get_by_car_tire_info(self, car_id: int):
        tire_list = session.query(CarTire).filter(CarTire.car_id == car_id).all()
        tire_dict = {}
        for tire in tire_list:
            tire_info = session.query(Tire.value, Tire.tire_type_id).filter(Tire.tire_id == tire.tire_id).first()
            if tire_info.tire_type_id == TireTypeEnum.front:
                tire_dict['front'] = tire_info.value
            tire_dict['rear'] = tire_info.value
        return tire_dict

    async def save(self, car_tire: CarTire) -> CarTire:
        session.add(car_tire)
        return car_tire