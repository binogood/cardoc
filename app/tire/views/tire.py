from fastapi import APIRouter

from app.tire.request.tire import CreateTireRequest
from app.tire.response.tire import CreateTireResponse
from app.tire.service.tire import TireService

from core.fastapi.schemas.response import ExceptionResponseSchema

tire_router = APIRouter()


@tire_router.post(
    "/create-tire",
    response_model=CreateTireResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create Tire"
)
async def create_tire(request: CreateTireRequest):
    return await TireService().create_tire(**request.dict())



