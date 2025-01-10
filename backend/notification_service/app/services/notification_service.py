
from app.providers.sse_provider import send_sse_notification
from app.providers.email_provider import send_email


def process_transaction_notification(event):
    user_id = event.get("user_id")
    transaction_id = event.get("transaction_id")
    amount = event.get("amount")

    subject = f"Transaction Confirmée - ID {transaction_id}"
    body = f"Votre transaction de {amount} a été confirmée."

    # Envoi de l'email
    send_email(f"user_{user_id}@example.com", subject, body)

    # Notification SSE
    send_sse_notification(user_id, body)

def process_blockchain_notification(event):
    user_id = event.get("user_id")
    transaction_hash = event.get("transaction_hash")

    subject = f"Blockchain Confirmée - Hash {transaction_hash}"
    body = f"Votre transaction blockchain a été confirmée avec le hash {transaction_hash}."

    # Envoi de l'email
    send_email(f"user_{user_id}@example.com", subject, body)

    # Notification SSE
    send_sse_notification(user_id, body)
