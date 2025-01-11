# EcoCoin Platform Documentation

## Overview

The EcoCoin Platform is a microservice-based architecture designed to facilitate transactions using Carbon MCO2 tokens. It enables users to manage wallets, perform transactions, track market prices, and interact with blockchain-based services. This platform also allows users to purchase carbon credits to offset their CO₂ emissions.

---

## Microservices Overview

### 1. API Gateway
- **Purpose**: Acts as the entry point for all client requests, routing them to appropriate microservices.
- **Technologies**: FastAPI
- **Responsibilities**:
  - Request routing
  - Authentication and authorization (via JWT/OAuth2)
  - Centralized error handling

### 2. User Service
- **Purpose**: Manages user accounts and wallets.
- **Database**: PostgreSQL (`user_service_db`)
- **Features**:
  - **Authentication**:
    - Endpoints: `/token` (generate JWT), `/users/me` (user info)
    - Passwords hashed with bcrypt
    - Secure sessions using JWT
  - **User Management**:
    - Create and manage users
    - Role management (seller, buyer)
  - **Wallet Management**:
    - Default wallets for supported currencies (USD, ETH, CARBON)
    - Operations: Create, update, and retrieve wallets
  - **Libraries**:
    - FastAPI, SQLAlchemy, bcrypt, jose, Alembic

### 3. Transaction Service
- **Purpose**: Handles transactions, including payments, transfers, and credit purchases.
- **Database**: PostgreSQL (`transaction_service_db`)
- **Features**:
  - Payment and transfer transaction workflows
  - Integration with Price and User Services

### 4. Price Service
- **Purpose**: Tracks market prices for MCO2 tokens and related currencies.
- **Database**: PostgreSQL (`price_service_db`)
- **Features**:
  - Fetch and store market prices via scraping or APIs

### 5. Blockchain Service
- **Purpose**: Manages blockchain-based transactions and token-related activities.
- **Features**:
  - Integration with Ethereum blockchain via Web3.py
  - Interaction with smart contracts (CarbonAccount, CarbonPayment, CarbonStaking, CarbonToken)

### 6. Notification Service
- **Purpose**: Sends transaction updates and blockchain event notifications.
- **Technologies**: Kafka for event-driven architecture

---

## Key Processes

### 1. User Registration
- Endpoint: `POST /users`
- Validates and stores user data.

### 2. Wallet Management
- Endpoint: `GET /users/{id}/wallets`
- Retrieve or update wallet details.

### 3. Transactions
- Workflow:
  - Validate wallet balances
  - Fetch market prices
  - Update wallet balances
  - Record transactions in the database

### 4. Market Price Updates
- Scrapes data from CoinGecko or APIs.
- Stores prices in `price_service_db`.

### 5. Blockchain Interaction
- Processes blockchain transactions using Web3.

### 6. Notifications
- Uses Kafka to notify users about transaction updates.

---

## Deployment

### Prerequisites
- Docker and Docker Compose
- PostgreSQL
- Python (with `venv` for virtual environments)

### Steps
1. **Setup Databases**:
   - Create databases: `user_service_db`, `transaction_service_db`, `price_service_db`
   - Apply migrations with Alembic: `alembic upgrade head`

2. **Build and Run Microservices**:
   - Use Docker Compose: `docker-compose up --build`

3. **Start Kafka and Zookeeper**:
   - Zookeeper: `zookeeper-server-start.sh config/zookeeper.properties`
   - Kafka: `kafka-server-start.sh config/server.properties`

4. **Verify Services**:
   - Test endpoints using Postman.

---

## Future Enhancements
- Real-time price updates via WebSocket.
- Expanded currency support.
- Enhanced user notifications.

---

## Messages

### Synchronous (REST API)
- Validate users: `GET /users/{user_id}`
- Update wallets: `PUT /users/{user_id}/wallets`

### Asynchronous (Kafka)
- Wallet updates post-transaction.
- Transaction status notifications.
