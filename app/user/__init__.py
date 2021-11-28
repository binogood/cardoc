from fastapi import APIRouter

from app.user.views import sub_router

user_router = APIRouter()
user_router.include_router(sub_router, prefix="/user", tags=["User"])

__all__ = ["user_router"]