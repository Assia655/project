from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_price_update(currency: str, price: float):
    message = {"currency": currency, "price": price}
    producer.send("market-prices", value=message)
