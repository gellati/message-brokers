import kafka as _k
from kafka import KafkaConsumer
import json
from data import KAFKA_TOPIC, KAFKA_SERVERS

api_version = _k.__version__.split(".")

def json_deserializer(data):
    return json.loads(data.decode("utf-8"))
#    return json.loads(data).encode("utf-8") # as bytes

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVERS,
    value_deserializer = json_deserializer
)

for message in consumer:
   print(message.value)
