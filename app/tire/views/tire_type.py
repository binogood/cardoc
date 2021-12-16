from fastapi import APIRouter, Depends

from app.tire.request.tire_type import CreateTireTypeRequest
from app.tire.response.tire_type import CreateTireTypeResponse
from app.tire.service.tire_type import TireTypeService

from core.fastapi.schemas.response import ExceptionResponseSchema
from core.fastapi.dependencies.permission import PermissionDependency, IsAdmin

tire_type_router = APIRouter()


@tire_type_router.post(
    "/create-tire-type",
    response_model=CreateTireTypeResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([IsAdmin]))],
    summary="Create Tire Type"
)
async def create_tire_type(request: CreateTireTypeRequest):
    return await TireTypeService().create_tire_type(request.value)