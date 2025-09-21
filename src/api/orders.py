from fastapi import APIRouter, HTTPException, status

from src.api.dependencies import SessionDep, PaginationDep, AuthDep
from src.repository.orders import OrdersRepository
from src.schemas.orders import OrderScheme

router = APIRouter()

@router.get("/api/orders",
            tags=["order-controller"],
            summary="get_orders",
            dependencies=[AuthDep]
            )
async def get_all(session: SessionDep,
                  pagination: PaginationDep
                  ):
    orders = await OrdersRepository.get_orders(session, pagination)
    return orders

@router.get("/api/orders/{order_id}",
            tags=["order-controller"],
            summary="get_order",
            dependencies=[AuthDep]
            )
async def get_one(order_id:int,
                  session: SessionDep
                  ):
    order = await OrdersRepository.get_order(order_id, session)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Order not found"
                            )
    return order


@router.post("/api/orders",
             tags=["order-controller"],
             summary="create_order",
             dependencies=[AuthDep]
             )
async def create_one(data: OrderScheme,
                     session: SessionDep
                     ):
    created_order = await OrdersRepository.create_order(data, session)
    return created_order

@router.put("/api/orders/{order_id}",
            tags=["order-controller"],
            summary="update_order",
            dependencies=[AuthDep]
            )
async def update_one(
        order_id: int,
        data: OrderScheme,
        session: SessionDep
):
    updated_order = await OrdersRepository.update_order(order_id, data, session)
    if updated_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Order not found"
                            )
    return updated_order

@router.delete("/api/orders/{order_id}",
               tags=["order-controller"],
               summary="delete_order",
               dependencies=[AuthDep]
               )
async def delete_one(order_id: int,
                     session: SessionDep
                     ):
    await OrdersRepository.delete_order(order_id, session)
    return {"message": "No Content"}