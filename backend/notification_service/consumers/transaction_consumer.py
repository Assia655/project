import asyncio
from aiokafka import AIOKafkaConsumer

class TransactionConsumer:
    def __init__(self):
        self.consumer = AIOKafkaConsumer(
            'transaction_events',
            loop=asyncio.get_event_loop(),
            bootstrap_servers='localhost:9092',
            group_id='transaction_group'
        )

    async def consume(self):
        await self.consumer.start()
        try:
            async for message in self.consumer:
                print(message.value)
        finally:
            await self.consumer.stop()

    # Modification : Retourne bien la coroutine de `consume`
    async def start(self):
        await self.consume()

# Dans la fonction de démarrage de ton application FastAPI
async def startup_event():
    print("Starting notification service...")
    transaction_consumer = TransactionConsumer()

    # Crée la tâche asynchrone correctement en utilisant await
    await transaction_consumer.start()
