from fastapi import APIRouter

from app.tire.views import sub_router

tire_router = APIRouter()
tire_router.include_router(sub_router, prefix="/tire", tags=["Tire"])

__all__ = ["tire_router"]