from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "transaction_events",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

def process_transaction_events():
    """Process events received from Kafka."""
    for message in consumer:
        event = message.value
        print(f"Received event: {event}")
