from fastapi import APIRouter

from api.controllers import ticker_kline_controller

routers = APIRouter(
    prefix="/api/v1",
    tags=["Orderservice"],
    responses={404: {"description": "Not found"}},
)

routers.include_router(ticker_kline_controller.router)
