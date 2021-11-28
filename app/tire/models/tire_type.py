from typing import Union, NoReturn

from sqlalchemy import Column, Integer, String

from cardoc.core.db.session import Base


class TireType(Base):
    __tablename__ = "tire_types"

    tire_type_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=30), unique=True, nullable=False)

    def create(self, name: str) -> Union['TireType', NoReturn]:
        return TireType(name=name)