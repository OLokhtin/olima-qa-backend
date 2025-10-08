from fastapi import APIRouter

from src.repository.rabbit import produce_order
from src.schemas.orders import OrderScheme

router = APIRouter()

@router.post("/api/rabbit/create_order",
            tags=["rabbit-controller"],
            summary="produce_new_order"
            )
def produce_new_order(data: OrderScheme):
    produce_order(data, "new_orders")
    return {"message": "OK"}

@router.post("/api/rabbit/update_order",
            tags=["rabbit-controller"],
            summary="produce_updated_order"
            )
def produce_updated_order(data: OrderScheme):
    produce_order(data, "updated_orders")
    return {"message": "OK"}