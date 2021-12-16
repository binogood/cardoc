from fastapi import APIRouter, Depends

from app.car.request.car import CreateCarRequest
from app.car.response.car import CreateCarResponse
from app.car.service.car import CarService

from core.fastapi.schemas.response import ExceptionResponseSchema
from core.fastapi.dependencies.permission import (
    PermissionDependency,
    IsAdmin,
)

car_router = APIRouter()


@car_router.post(
    "/create-car",
    response_model=CreateCarResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAdmin]))],
    summary="Create Car",
)
async def create_car(request: CreateCarRequest):
    return await CarService().create_car(**request.dict())