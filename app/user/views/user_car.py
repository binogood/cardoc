from fastapi import APIRouter

from typing import List, Optional

from app.user.request.user_car import (
    CreateUserCarDetailRequest,
)
from app.user.response.user_car import CreateUserCarResponse, GetUserCarResponse
from app.user.service.user_car import UserCarService

from core.fastapi.schemas.response import ExceptionResponseSchema

user_car_router = APIRouter()


@user_car_router.post(
    "/create-user-car",
    response_model=List[CreateUserCarResponse],
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create User Car",
)
async def create_user_car(request: List[CreateUserCarDetailRequest]):
    return await UserCarService().create_user_car(**request.dict())


@user_car_router.get(
    "/get-user-car",
    response_model=GetUserCarResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Get User Car",
)
async def get_user_car(trimId: Optional[int], name: Optional[str]):
    return await UserCarService().get_user_car(trimId=trimId, name=name)