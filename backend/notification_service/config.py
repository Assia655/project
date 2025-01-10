class Config:
    # Kafka
    KAFKA_BROKER = "localhost:9092"
    TRANSACTION_TOPIC = "transaction_events"
    BLOCKCHAIN_TOPIC = "blockchain_events"
    NOTIFICATION_TOPIC = "notification_events"

    # Notification Settings
    EMAIL_SMTP_SERVER = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_USERNAME = "salmadoumi111@gmail.com"
    EMAIL_PASSWORD = "sdoumi@2003"
    SMS_API_URL = "https://sms-provider.com/send"
    SMS_API_KEY = "your_sms_api_key"

