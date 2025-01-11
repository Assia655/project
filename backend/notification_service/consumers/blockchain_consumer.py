from kafka import KafkaConsumer
import json
from app.services.notification_service import process_blockchain_notification
from app.config import Config

class BlockchainConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            Config.BLOCKCHAIN_TOPIC,
            bootstrap_servers=Config.KAFKA_BROKER,
            value_deserializer=lambda v: json.loads(v.decode('utf-8')),
            group_id="notification_service_group"
        )

    def start(self):
        for message in self.consumer:
            event = message.value
            print(f"Blockchain event received: {event}")
            process_blockchain_notification(event)
