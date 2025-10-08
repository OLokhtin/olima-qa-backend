from pika import ConnectionParameters, BlockingConnection, BasicProperties
import json

from src.schemas.orders import OrderScheme

connection_params = ConnectionParameters(
    host="localhost",
    port=5672
)

def produce_order(data: OrderScheme, order_queue: str):
    order_data = data.model_dump_json()
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue=order_queue)
            ch.basic_publish(
                exchange="",
                routing_key=order_queue,
                body=json.dumps(order_data),
                properties=BasicProperties(
                    delivery_mode=2,
                    content_type='application/json'
                )
            )