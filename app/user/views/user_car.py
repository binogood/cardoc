from fastapi import APIRouter, Depends, Request

from typing import List, Optional

from app.user.request.user_car import (
    CreateUserCarDetailRequest,
)
from app.user.response.user_car import CreateUserCarResponse, GetUserCarResponse
from app.user.service.user_car import UserCarService

from core.fastapi.dependencies.permission import PermissionDependency, IsAuthenticated
from core.fastapi.schemas.response import ExceptionResponseSchema


user_car_router = APIRouter()


@user_car_router.post(
    "/create-user-car",
    response_model=List[CreateUserCarResponse],
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
    summary="Create User Car",
)
async def create_user_car(request: List[CreateUserCarDetailRequest], user_info: Request):
    return await UserCarService().create_user_car(user_info, request)


@user_car_router.get(
    "/get-user-car",
    response_model=GetUserCarResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))],
    summary="Get User Car",
)
async def get_user_car(trim_id: Optional[int], name: Optional[str]):
    return await UserCarService().get_user_car(trim_id=trim_id, name=name)