
from typing import Union, NoReturn

from sqlalchemy import Column, Integer, ForeignKey

from cardoc.core.db.session import Base


class CarTire(Base):
    __tablename__ = "car_tires"

    car_tire_id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('cars.car_id'), nullable=False)
    tire_id = Column(Integer, ForeignKey('tires.tire_id'), nullable=False)

    def create(self, car_id: int, tire_id: int) -> Union["CarTire", NoReturn]:
        return CarTire(car_id=car_id, tire_id=tire_id)