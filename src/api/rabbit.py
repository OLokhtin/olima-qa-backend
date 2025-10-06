# http://localhost:15672
from pika import ConnectionParameters, BlockingConnection

connection_params = ConnectionParameters(
    host="localhost",
    port=5672
)

def main():
    with BlockingConnection(connection_params) as conn:
        with conn.channel() as ch:
            ch.queue_declare(queue="new_orders")
            ch.basic_publish(
                exchange="",
                routing_key="new_orders",
                body="Hello World"
            )

if __name__ == "__main__":
    main()