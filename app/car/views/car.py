from fastapi import APIRouter, Header
from typing import Optional

from app.car.request.car import CreateCarRequest
from app.car.response.car import CreateCarResponse
from app.car.service.car import CarService

from cardoc.core.fastapi.schemas.response import ExceptionResponseSchema

car_router = APIRouter()


@car_router.post(
    "/create_car",
    response_model=CreateCarResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create Car",
)
async def create_car(request: CreateCarRequest, token: Optional[str] = Header(None)):
    return await CarService().create_car(token, **request.dict())


# @car_router.get(
#     "/{trim_id}",
#     response_model=GetCarRequest,
#     responses={"404": {"model": ExceptionResponseSchema}},
#     summary="Get Car",
# )
# async def get_car(request: GetCarRequest):
#     return await CarService().login_car