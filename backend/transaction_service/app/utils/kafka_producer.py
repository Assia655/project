from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_transaction_event(event_type: str, data: dict):
    """Send transaction-related events to Kafka."""
    producer.send("transaction_events", {"event_type": event_type, "data": data})
    producer.flush()
