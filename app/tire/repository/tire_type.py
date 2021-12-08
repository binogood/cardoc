from abc import ABCMeta, abstractmethod
from typing import Optional

from app.tire.models.tire_type import TireType
from core.db.session import session


class TireTypeRepo:
    __metaclass__ = ABCMeta

    @abstractmethod
    async def get_by_tire_type(self, name: str) -> Optional[TireType]:
        pass

    @abstractmethod
    async def save(self, tire_type: TireType) -> TireType:
        pass


class TireTypeMySQLRepo(TireTypeRepo):
    async def get_by_tire_type(self, name: str) -> Optional[TireType]:
        return session.query(TireType).filter(TireType.name == name).first()

    async def save(self, tire_type: TireType) -> TireType:
        session.add(tire_type)
        return tire_type
