notification_service/
├── consumers/                      
│   ├── __init__.py
│   ├── transaction_consumer.py     
│   ├── blockchain_consumer.py      
│   ├── user_consumer.py            
│   ├── sse_consumer.py             
│
├── logs/                           
│   ├── notification_service.log    
│
├── providers/                      
│   ├── __init__.py
│   ├── email_provider.py           
│   ├── sse_provider.py             
│
├── services/                       
│   ├── __init__.py
│   ├── notification_service.py     
│   ├── email_service.py            
│
├── templates/                      
│   ├── notification_email.html     
│   ├── notification_email.txt      
│
├── config.py                       
├── logger.py                       
├── main.py                         
├── Dockerfile                      
├── requirements.txt         
└── test_main.http                  





+--------------------+       +--------------------+       +--------------------+
|  User Service      |       | Transaction Service|       | Blockchain Service |
|  (users, wallets)  |       | (transactions)     |       | (blockchain events)| 
+--------------------+       +--------------------+       +--------------------+
         |                            |                             |
         +----------------------------+-----------------------------+
                                      |
                         Kafka Message Broker
                    (Topics: transaction_events, blockchain_events)
                                      |
                                      v
+-------------------------------------------------------------------------+
|                          Notification Service                           |
|                                                                         |
|  +---------------------+        +-------------------+   +-------------+|
|  | Transaction Consumer| -----> | Notification Logic|-->| Email/SSE   ||
|  +---------------------+        +-------------------+   +-------------+|
|                                                                         |
|  +---------------------+        +-------------------+   +-------------+|
|  | Blockchain Consumer | -----> | Notification Logic|-->| Email/SSE   ||
|  +---------------------+        +-------------------+   +-------------+|
|                                                                         |
|                   +-----------------------------------+                 |
|                   |        Logging Service           |                 |
|                   +-----------------------------------+                 |
+-------------------------------------------------------------------------+
