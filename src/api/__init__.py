from fastapi import APIRouter

from src.api.orders import router as orders_router
from src.api.auth import router as auth_router


main_router = APIRouter()

main_router.include_router(auth_router)
main_router.include_router(orders_router)