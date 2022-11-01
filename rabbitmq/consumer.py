import pika

from constants import QUEUE
from constants import HOST

def callback(ch, method, properties, body):
    print(f"[x] received {body.decode()}")

queue = QUEUE
connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))

channel = connection.channel()
channel.queue_declare(
    queue=queue,
)

channel.basic_consume(
    queue=queue,
    auto_ack = True,
    on_message_callback = callback
)

channel.start_consuming()