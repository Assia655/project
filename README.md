# EcoCoin Project
Version: 1.0

---

## Project Overview
EcoCoin is a platform that enables trading carbon tokens, with each token representing 1 ton of CO₂. This initiative aims to reduce carbon emissions by allowing companies to trade carbon credits, promoting sustainable practices. Customers can purchase tokens using ETH or EUR, depending on their wallet configuration.
## Logo:
![App Screenshot](./img/logo.png)
---

## Core Idea
- Each EcoCoin represents 1 ton of CO₂.
- Companies can sell or buy EcoCoins based on market conditions.
- Tokens can be purchased with cryptocurrency (ETH) or fiat currency (EUR).

---
## Team Members
- Frontend: Niama Aqarial
- Backend: Salma Doumi
- DevOps: Assia Haimeur
- Blockchain: Karima Ahdich
- Data Analyst: Chaimae Ababri

---

## Technologies Used
- Frontend: Angular, Angular Material
- Backend: FastApi
- Blockchain: Ethereum-based smart contracts
- DevOps: Docker, CI/CD pipelines
- Data Analysis: Python, Pandas, Machine Learning

---

### Setup Instructions
1. Requirements:
   - Node.js (v16 or later)
   - Angular CLI
   - Docker (for deployment)

2. Steps to Run the Project:
   - Clone the repository:
     git clone https://github.com/Assia655/project.git
     cd project
   - Follow the setup instructions in the respective folders (frontend, backend, etc.).

---

# Frontend Contribution by Niama Aqarial
## Features:
  - **Home Page**: Introduces the EcoCoin platform, the sponsors, About information and contact details.
    - Home :
    ![App Screenshot](./img/home.png)
    - Sponsors :
    ![App Screenshot](./img/sponsors.png)
    - About us :
    ![App Screenshot](./img/aboutus.png)
    - Contact :
    ![App Screenshot](./img/contact.png)
  - **Login**: Contains a Form for the users to login.
    ![App Screenshot](./img/login.png)
  - **signup**: Created for new users to signup
    ![App Screenshot](./img/signup.png)
  - **dashboard**: Provides a form for inquiries or feedback.
    - Part 1 :
    ![App Screenshot](./img/dashboard_1.png)
    - Part 2 :
    ![App Screenshot](./img/dashboard_2.png)
    - Part 3 :
    ![App Screenshot](./img/dashboard_3.png)
  - **user profile**: Dedicated to display the user profile information.
    - Wallets :
    ![App Screenshot](./img/profile_1.png)
    - Profile :
    ![App Screenshot](./img/profile_2.png)
  - **users_list**: this page is for the admin to help manage the users. It includes showing or editing there profile and also deleting them from the database.
    ![App Screenshot](./img/users_list.png)
  - **Edit user** : For editing the user profile information
    ![App Screenshot](./img/edit_user.png)
## Technologies :
  - Angular for building the interface.
  - Angular Material combined with CSS and HTML for styling and components.
## Frontend Setup Instructions:
  1. Navigate to the `frontend` directory:
     ```
     cd frontend
     ```
  2. Install dependencies:
     ```
     npm install
     ```
  3. Start the development server:
     ```
     ng serve
     ```
  4. Open your browser at:
     ```
     http://localhost:4200
     ```
## Angular Routes:
- /home
- /user
- /login
- /signup
- /users_list
- /dashboard
---
# Blockchain Contribution by Karima Ahdich
## Smart Contract Deployment and Functionality Report

### Solidity - The Language Used

Solidity is a high-level programming language used for writing smart contracts on the Ethereum blockchain. It is similar to JavaScript, but specifically designed to interact with the blockchain. Solidity allows you to create smart contracts, which are autonomous programs stored and executed on the blockchain.

### Main Features of Solidity:

- **Smart Contracts**: Solidity allows you to define smart contracts, which are programs that execute automatically when certain conditions are met. These contracts can manage transactions, digital assets, or interact with other contracts on the blockchain.

- **Data Types**:
    - uint, int: Unsigned and signed integers.
    - address: Types of addresses for Ethereum accounts.
    - bool: Boolean values.
    - string: Strings of characters.
    - mapping: Mappings (dictionaries) that link keys to values, for example, to track the balance of users.

- **Modifiers**: Solidity allows the use of modifiers, which are reusable functions that manage access permissions. For example, the `onlyOwner` modifier restricts access to certain functions to the contract’s administrator.

- **Events**: Events are used to notify external applications about state changes in contracts. For example, an event might be triggered when a user is registered, or when carbon credits are added.

## Contract `CarbonAccount.sol`

### Features:

- **User Registration**: The contract allows registering users by associating an Ethereum address with wallet information. The wallet address is initially set to 0x0 during registration.
- **Wallet Association**: After registering a user, a wallet address can be associated with the user through the `linkWallet()` function.
- **Carbon Credit Credit**: The `creditCarbon()` function allows the owner to add carbon credits for a specific user.
- **Ownership Management**: Only the owner of the contract (the address that deployed the contract) can call sensitive functions such as `registerUser`, `linkWallet`, and `creditCarbon`.
![App Screenshot](./img/edit_user.png)

## Contract `CarbonToken.sol`
### Features:

- **ERC-20 Token**: This contract creates an ERC-20 token called `CarbonToken` with the symbol `CTK`.
- **Carbon Credit Creation**: The owner of the contract can call the `mint(address to, uint256 amount)` function to create tokens for a user.
- **Carbon Credit Transfer**: The `transferCarbon(address to, uint256 amount)` function allows transferring carbon credits between users.
- **Carbon Credit Burning**: The `burn(address from, uint256 amount)` function allows burning carbon credits, removing them from the system.
- **Carbon Credit Verification**: The `balanceOfCarbon(address user)` function allows checking the carbon credits held by a user.
## Contract `CarbonStaking.sol`

### Features:

- **Carbon Credit Staking**: This contract allows users to stake their carbon credits to participate in ecological projects such as tree planting.
- **Unstaking Carbon Credits**: The `unstake()` function allows users to withdraw their staked credits after a defined staking period.
- **Staked Credit Verification**: The `getStakedBalance(address user)` function allows checking the amount of carbon credits staked by a user.

## Contract `CarbonPayement.sol`

### Features:

- **Payment Management**: This contract allows users to make payments using traditional methods, such as credit cards or bank transfers, to purchase carbon credits.
- **Conversion of Funds into Tokens**: The `convertToCarbonTokens()` function allows converting funds (such as Ethereum) into carbon credits.
- **Payment Tracking**: The `trackPayment()` function allows tracking the payment history made by users.

## Deployment with MetaMask, Hardhat, and Sepolia

The 4 smart contracts were initially created in Remix, an online IDE for Solidity development. After writing and compiling the contracts, Remix was connected to MetaMask through the Injected Web3 provider. This connection allowed Remix to interact with the Ethereum network using the accounts available in MetaMask. With MetaMask acting as the wallet and providing the necessary network connection, the contracts were deployed on a chosen network, whether local or testnet (Sepolia). This setup enabled seamle...

### Deployment with MetaMask and Hardhat:

### Prerequisites:

- **MetaMask** is used to manage Ethereum accounts and connect to Ethereum networks.
- **Hardhat** is used for deploying and testing the contracts locally or on a testnet.

### Setting up Hardhat:
1. Install Hardhat: `npm install --save-dev hardhat`.
2. Create a deployment script in the `scripts` folder.
3. Deploy to a local network using the command:
    ```bash
    npx hardhat run --network localhost
    ```

### Deployment on Sepolia Testnet:

- Configuring Sepolia Network:
1. Configure Hardhat to connect to Sepolia in the `hardhat.config.js` file.
2. Get test ETH for Sepolia via a faucet. I used [this link](https://cloud.google.com/application/web3/faucet/ethereum/sepolia).
3. Deploy to Sepolia using the command:
    ```bash
    npx hardhat run scripts/deploy.js --network sepolia
    ```

### Connecting with MetaMask:
- **MetaMask** was configured to interact with the deployed contracts on the local network or the Sepolia testnet.
- **MetaMask** was used to manage accounts and interact with the Ethereum blockchain.

### Integration with Web3.py

## Installing Web3.py:

You installed Web3.py with the following command:
```bash
pip install web3
```

## Connecting to MetaMask:
**Web3.py** was used to interact with the contracts through MetaMask by using the `window.ethereum` instance to connect via the browser.

```python
from web3 import Web3

Web3_provider="http://127.0.0.1:8545"

web3=Web3(Web3.HTTPProvider(Web3_provider))

contract_address = 'the contract address after deployment'

abi = [...] # Contract ABI “Abi du contract is in the remix compiler tab” 

if not web3.is_connected():
    print("Web3 not connected")
```

## Interacting with Contracts via Web3.py:

Example of calling a function in the contract with Web3.py:
```python
result = contract.functions.functionName().call()
print(result)
```

## Sending Transactions via Web3.py:
```python
txn = contract.functions.creditCarbon(user_address, 100).buildTransaction({
    'from': user_address,
    'gas': 2000000,
    'gasPrice': web3.toWei('20', 'gwei'),
    'nonce': web3.eth.getTransactionCount(user_address),
})

signed_txn = web3.eth.account.signTransaction(txn, private_key='')
txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

print(f'Transaction hash: {txn_hash.hex()}')
```
---
## Blockchain Test
![App Screenshot](./img/activity.PNG)
![App Screenshot](./img/contract%20deployee.PNG)
![App Screenshot](./img/hardhat.PNG)
![App Screenshot](./img/wallet%20metamask.PNG)
![App Screenshot](./img/teste%20stake().PNG)
![App Screenshot](./img/teste%20mint().PNG)
---
# DevOps - Management and Deployment of Microservices Contribution by Assia Haimeur

**About the Project**

In this project, my primary role was as a **DevOps Engineer**. I managed the entire lifecycle of the microservices, from creating Dockerfiles to deploying the microservices on the cloud using **Azure Kubernetes Service (AKS)**. This document outlines the technical steps I followed, the tools used, and the results achieved.

---

**Project Architecture**

The architecture of this project includes multiple interconnected microservices (API Gateway, User Service, Transaction Service, etc.), each exposed on a unique port. Below is a summary illustration of the architecture:



The deployment involves a single Azure Kubernetes Service (AKS) cluster with one node hosting multiple pods. Each pod contains a container for the respective microservice. The services communicate with each other via Kubernetes networking, and the API Gateway uses a LoadBalancer service to expose the application to external traffic.

---

**Work Environment**

- Installed Tools:

1. **Docker Desktop**: For creating and testing containers locally.
2. **kubectl** and **Kind**: For managing Kubernetes clusters locally.
3. **GitHub Actions**: To implement a CI/CD pipeline.
4. **Azure Kubernetes Service (AKS)**: For final deployment on the cloud.
5. **Docker Hub**: Used as a registry to store and share Docker images.

---

## Technical Steps

### Creating Dockerfiles

I created **Dockerfiles** for each microservice. Here is an example of a Dockerfile used for Python-based services:

```dockerfile
FROM python:3.10-slim AS base

# Define the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file containing dependencies
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port used by the FastAPI application
EXPOSE 8001

# Define the startup command for Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
```

Each microservice was exposed on a unique port to avoid conflicts.

### List of Ports Used

- **User Service**: Port 8004
- **Transaction Service**: Port 8003
- **Price Service**: Port 8002
- **API Gateway**: Port 8005
- **Frontend**: Port 3000
- **Blockchain Service**: Port 8001
- **Notification Service**: Port 8006

### Testing Containers with Docker Compose

I wrote a `docker-compose.yml` file to test the interconnection of microservices locally. Here's a snippet:

```yaml
version: "3.9"
services:
  user_service:
    build:
      context: ./backend/user_service
    ports:
      - "8004:8004"
    environment:
      - DB_HOST=user_db
  user_db:
    image: postgres:13
    ports:
      - "5432:5432"
```

Commands used:

- Build containers: `docker-compose build`
- Run containers: `docker-compose up`

### Creating Kubernetes Files

#### Why Use PVC for Databases

Persistent Volume Claims (PVCs) ensure that the database data persists even if the pods are terminated or restarted. This provides resilience and durability for critical data.

#### Service Types

- **NodePort**: Used for testing services locally and providing direct access to the services.
- **ClusterIP**: Default service type for internal communication between microservices.
- **LoadBalancer**: Used for exposing the API Gateway to external traffic, enabling users to access the application.

#### Example YAML Files

Deployment for User Service:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 2
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
      - name: user-service
        image: dockerhub_username/user-service:latest
        ports:
        - containerPort: 8004
```

Persistent Volume Claim for Database:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: user-db-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

Service for API Gateway:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-gateway
spec:
  type: LoadBalancer
  selector:
    app: api-gateway
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8005
```

### Deployment with AKS (Azure Kubernetes Service)

#### Steps Followed:

1. Create a Kubernetes cluster on Azure:
   ```bash
   az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 1 --enable-addons monitoring --generate-ssh-keys
   ```
2. Connect to the cluster:
   ```bash
   az aks get-credentials --resource-group myResourceGroup --name myAKSCluster
   ```
3. Deploy the microservices to the Azure cluster:
   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

### CI/CD Pipeline with GitHub Actions

I created a GitHub Actions workflow to automate the process of building and pushing Docker images to Docker Hub, as well as local deployment with Kind.

Example `github-actions.yml` file:

```yaml
name: CI/CD Pipeline
on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout Code
      uses: actions/checkout@v3
    - name: Log in to Docker Hub
      run: echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
    - name: Build and Push Docker Images
      run: |
        docker build -t dockerhub_username/user-service ./backend/user_service
        docker push dockerhub_username/user-service
  deploy-kind:
    runs-on: ubuntu-latest
    steps:
    - name: Deploy to Kind Cluster
      run: |
        kubectl apply -f deployment.yaml
```

---
![App Screenshot](./img/devops.jpg)
---

## Results Achieved

1. not All tested microservices were successfully containerized and deployed (User Service, Transaction Service, Price Service, and API Gateway) but it still (blockchain service, notification service , front end ) not deployed because my colleges didn't coplete them and they pushed all yesterday so a didn't found time to manage all of this .
2. A functional CI/CD pipeline was established with GitHub Actions for building, pushing, and deployment  .
3. Deployment of microservices to a Kubernetes cluster using both Kind (local) and AKS (cloud).

---

## Future Improvements

1. Migrate to a more scalable cloud solution.
2. Deploy the full application, including Blockchain and Notification Services, on AWS.
3. Implement advanced monitoring with Prometheus and Grafana.
4. Use Helm to simplify Kubernetes deployments.

---

Contact
For any questions or feedback, feel free to contact the team:
- Niama Aqarial (Frontend Developer): niama.aqarial@gmail.com
- Salma Doumi (Backend Developer) :
- Assia Haimeur (DevOps Engineer) : haimeurassia70@gmail.com
- Karima Ahdich (Blockchain Developer) : karimaahdich@gmail.com
- Chaimae Ababri (Data Analyst) : chaimaeababri14@gmail.com

