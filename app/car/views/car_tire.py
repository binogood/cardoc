from fastapi import APIRouter, Header
from typing import Optional

from app.car.request.car_tire import CreateCarTireRequest
from app.car.response.car_tire import CreateCarTireResponse
from app.car.service.car_tire import CarTireService

from cardoc.core.fastapi.schemas.response import ExceptionResponseSchema

car_tire_router = APIRouter()


@car_tire_router.post(
    "/create_car_tire",
    response_model=CreateCarTireResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create Car",
)
async def create_car_tire(request: CreateCarTireRequest, token: Optional[str] = Header(None)):
    return await CarTireService().create_car_tire(token, **request.dict())