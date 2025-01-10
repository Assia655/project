import logging

logging.basicConfig(
    filename="logs/notification_service.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_event(event):
    logging.info(f"Event processed: {event}")
