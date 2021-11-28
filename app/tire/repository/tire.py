from abc import ABCMeta, abstractmethod
from typing import Optional

from app.tire.models.tire import Tire
from cardoc.core.db.session import session


class TireRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_tire(self, value: str, tire_type_id: int) -> Optional[Tire]:
        pass

    async def get_by_tire_id(self, tire_id: int) -> Optional[Tire]:
        pass

    @abstractmethod
    async def save(self, tire: Tire) -> Tire:
        pass


class TireMySQLRepo(TireRepo):
    async def get_by_tire(self, value: str, tire_type_id: int) -> Optional[Tire]:
        return session.query(Tire).filter(
            Tire.value == value,
            Tire.tire_type_id == tire_type_id
        ).first()

    async def get_by_tire_id(self, tire_id: int) -> Optional[Tire]:
        return session.query(Tire.tire_id).filter(Tire.tire_id == tire_id)

    async def save(self, tire: Tire) -> Tire:
        session.add(tire)
        return tire






