from fastapi import APIRouter, Depends

from app.tire.request.tire import CreateTireRequest
from app.tire.response.tire import CreateTireResponse
from app.tire.service.tire import TireService

from core.fastapi.schemas.response import ExceptionResponseSchema
from core.fastapi.dependencies.permission import PermissionDependency, IsAdmin

tire_router = APIRouter()


@tire_router.post(
    "/create-tire",
    response_model=CreateTireResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAdmin]))],
    summary="Create Tire"
)
async def create_tire(request: CreateTireRequest):
    return await TireService().create_tire(**request.dict())



