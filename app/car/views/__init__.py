from fastapi import APIRouter

from .car import car_router
from .car_tire import car_tire_router

sub_router = APIRouter()
sub_router.include_router(car_router, prefix="", tags=["Car"])
sub_router.include_router(car_tire_router, prefix="", tags=["Car"])

__all__ = ["sub_router"]