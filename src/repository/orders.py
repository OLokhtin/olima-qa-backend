from sqlalchemy import select, delete, update

from src.api.dependencies import SessionDep, PaginationDep
from src.models.orders import OrderModel
from src.schemas.orders import OrderScheme

class OrdersRepository:
    @classmethod
    async def get_orders(cls,
                            session: SessionDep,
                            pagination: PaginationDep
                            ):
        query = (select(OrderModel)
                 .limit(pagination.limit)
                 .offset(pagination.offset)
         )
        result = await session.execute(query)
        orders = result.scalars().all()
        return orders

    @classmethod
    async def get_order(cls,
                          order_id: int,
                          session: SessionDep
                          ):
        query = (select(OrderModel)
                 .filter(OrderModel.order_id == order_id)
                 )
        result = await session.execute(query)
        order = result.scalars().first()
        return order

    @classmethod
    async def create_order(cls,
                             data: OrderScheme,
                             session: SessionDep
                             ):
        new_order = OrderModel(
            status=data.status,
            customer_full_name=data.customer_full_name,
            customer_phone=data.customer_phone,
            customer_email=data.customer_email,
            delivery_address=data.delivery_address,
            delivery_date=data.delivery_date,
            total_amount=data.total_amount
        )
        session.add(new_order)
        await session.flush()
        await session.commit()
        return new_order

    @classmethod
    async def update_order(cls,
                             order_id: int,
                             data: OrderScheme,
                             session: SessionDep
                             ):
        query = ((update(OrderModel).
                  where(OrderModel.order_id == order_id)).
                 values(
            status=data.status,
            customer_full_name=data.customer_full_name,
            customer_phone=data.customer_phone,
            customer_email=data.customer_email,
            delivery_address=data.delivery_address,
            delivery_date=data.delivery_date,
            total_amount=data.total_amount
        ).
                 returning(OrderModel)
                 )
        result = await session.execute(query)
        await session.commit()
        updated_order = result.scalars().first()
        return updated_order

    @classmethod
    async def delete_order(cls,
                             order_id: int,
                             session: SessionDep
                             ):
        query = (delete(OrderModel).
                 where(OrderModel.order_id == order_id)
                 )
        await session.execute(query)
        await session.commit()