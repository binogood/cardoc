from typing import Union, NoReturn

from sqlalchemy import Column, Integer, ForeignKey

from core.db.session import Base


class UserCar(Base):
    __tablename__ = "user_cars"

    user_car_id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.car_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)

    def create(self, car_id: int, user_id: int) -> Union["UserCar", NoReturn]:
        return UserCar(car_id=car_id, user_id=user_id)