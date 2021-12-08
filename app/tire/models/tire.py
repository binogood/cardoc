from typing import Union, NoReturn

from sqlalchemy import Column, Integer, String, ForeignKey

from core.db.session import Base


class Tire(Base):
    __tablename__ = "tires"

    tire_id = Column(Integer, primary_key=True, autoincrement=True)
    tire_type_id = Column(Integer, ForeignKey('tire_types.tire_type_id'), nullable=False)
    value = Column(String(length=50), unique=True, nullable=False)

    def create(self, value: str, tire_type_id: int) -> Union['Tire', NoReturn]:
        return Tire(value=value, tire_type_id=tire_type_id)




