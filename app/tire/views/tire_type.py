from fastapi import APIRouter

from app.tire.request.tire_type import CreateTireTypeRequest
from app.tire.response.tire_type import CreateTireTypeResponse
from app.tire.service.tire_type import TireTypeService

from cardoc.core.fastapi.schemas.response import ExceptionResponseSchema

tire_type_router = APIRouter()


@tire_type_router.post(
    "/create_tire_type",
    response_model=CreateTireTypeResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    summary="Create Tire Type"
)
async def create_tire_type(request: CreateTireTypeRequest):
    return await TireTypeService().create_tire_type(**request.dict())