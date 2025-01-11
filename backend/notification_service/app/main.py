from fastapi import FastAPI
from app.consumers.transaction_consumer import TransactionConsumer
from app.consumers.blockchain_consumer import BlockchainConsumer
import asyncio

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Starting notification service...")
    transaction_consumer = TransactionConsumer()
    blockchain_consumer = BlockchainConsumer()

    asyncio.create_task(transaction_consumer.start())
    asyncio.create_task(blockchain_consumer.start())

@app.get("/")
def health_check():
    return {"status": "Notification Service Running"}
