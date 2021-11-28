from fastapi import APIRouter

from .user import user_router
from .user_car import user_car_router

sub_router = APIRouter()
sub_router.include_router(user_router, prefix="", tags=["User"])
sub_router.include_router(user_car_router, prefix="", tags=["User"])

__all__ = ["sub_router"]