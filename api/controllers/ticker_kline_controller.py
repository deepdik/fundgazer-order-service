import datetime
from datetime import date

from fastapi import APIRouter


from api.models.general_models import Platforms


router = APIRouter(
    prefix="",
    tags=["dataHandler"],
    responses={404: {"description": "Not found"}},
)


@router.get("/test", response_description="")
async def test():
    return None
