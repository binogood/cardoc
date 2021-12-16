from fastapi import APIRouter, Depends

from app.car.request.car_tire import CreateCarTireRequest
from app.car.response.car_tire import CreateCarTireResponse
from app.car.service.car_tire import CarTireService

from core.fastapi.schemas.response import ExceptionResponseSchema
from core.fastapi.dependencies.permission import PermissionDependency, IsAdmin

car_tire_router = APIRouter()


@car_tire_router.post(
    "/create-car-tire",
    response_model=CreateCarTireResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAdmin]))],
    summary="Create Car",
)
async def create_car_tire(request: CreateCarTireRequest):
    return await CarTireService().create_car_tire(**request.dict())