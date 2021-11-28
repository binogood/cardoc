from fastapi import APIRouter

from .tire import tire_router
from .tire_type import tire_type_router

sub_router = APIRouter()
sub_router.include_router(tire_router, prefix="", tags=['Tire'])
sub_router.include_router(tire_type_router, prefix="", tags=['Tire'])

__all__ = ["sub_router"]