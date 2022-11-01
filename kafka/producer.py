from time import sleep
import kafka as _k
from kafka import KafkaProducer
import json, random
from data import KAFKA_TOPIC, KAFKA_SERVERS

messages = ['one', 'two', 'dog', 'koala']
timeout_in_seconds = 2
message_interval_in_seconds = 1
api_version = _k.__version__.split(".")

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers = KAFKA_SERVERS,
    value_serializer = json_serializer,
    api_version=(
        int(api_version[0]),
        int(api_version[1]),
        int(api_version[2])
    )
)

while True:
    message = random.choice(messages)
    future = producer.send(
        KAFKA_TOPIC,
        message
    )
    result = future.get(timeout=timeout_in_seconds)
    print(result)
    sleep(message_interval_in_seconds)
