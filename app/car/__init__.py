from fastapi import APIRouter

from app.car.views import sub_router

car_router = APIRouter()
car_router.include_router(sub_router, prefix="/car", tags=["Car"])

__all__ = ["car_router"]