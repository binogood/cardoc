from typing import Union, NoReturn

from sqlalchemy import Column, Integer, DateTime, func

from core.db.session import Base
from core.db.timestamp_mixin import TimestampMixin


class Car(Base, TimestampMixin):
    __tablename__ = "cars"

    car_id = Column(Integer, primary_key=True, autoincrement=True)
    trimId = Column(Integer, nullable=False)
    created_at = Column(
                        DateTime,
                        nullable=False,
                        default=func.utc_timestamp(),
                        onupdate=func.utc_timestamp(),
                 )
    updated_at = Column(
                        DateTime,
                        nullable=False,
                        default=func.utc_timestamp(),
                        onupdate=func.utc_timestamp(),
                 )

    def create(self, trimId: int) -> Union["Car", NoReturn]:
        return Car(trimId=trimId)

