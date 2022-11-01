import pika, json, os
from constants import QUEUE
from constants import HOST

#url = os.environ.get('AMQP_URL', 'amqp://guest:guest@localhost:5672')
#params = pika.URLParameters(url)

connection = pika.BlockingConnection(pika.ConnectionParameters(HOST))

channel = connection.channel()

message = 'hello'

channel.queue_declare(queue=QUEUE)
channel.basic_publish(
    exchange='',
    routing_key=QUEUE,
    body=json.dumps(message),
    properties=(
        pika.BasicProperties(delivery_mode=2)
    )
)

connection.close()