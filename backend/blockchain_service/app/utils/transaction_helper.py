from web3 import Web3
from app.utils.contracts_loader import load_contract
from app.utils.web3_provider import web3
import asyncio

# Charger les contrats intelligents
carbon_account = load_contract(web3, "CarbonAccount.json", "0x86cFd7B586f1a2a7eE34791d56Fd397aD15187ed")
carbon_payment = load_contract(web3, "CarbonPayment.json", "0xEADacF21b70c3a8FAbE27DcB3A6237a6DE86889b")
carbon_staking = load_contract(web3, "CarbonStaking.json", "0x9a19C34E49cBa80d72D1B25DA21831D285E27081")
carbon_token = load_contract(web3, "CarbonToken.json", "0x1C26029981dc109eb1EB6F403Ad4AEDFd29E7f34")

# Adresse utilisateur et clé privée (remplacez par des variables sécurisées)
USER_ADDRESS = "0xA09e8aD094a059C12a6227ef8bE5d00527891304"
PRIVATE_KEY = "ea4d8d6348a7cd9240968cbaaa1447197fa82d4f39fbebb512a83a748cab0774"

# Fonction pour signer et envoyer une transaction
async def send_transaction(contract_function, user_address, private_key, value=0):
    # Construire la transaction
    transaction = contract_function.buildTransaction({
        'from': user_address,
        'value': value,  # ETH envoyé (en Wei)
        'gas': 3000000,
        'gasPrice': web3.toWei('20', 'gwei'),
        'nonce': web3.eth.getTransactionCount(user_address),
    })
    # Signer la transaction
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
    # Envoyer la transaction
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    return web3.eth.waitForTransactionReceipt(tx_hash)

# 1. Fonctionnalités du contrat CarbonAccount
async def register_user(user_address):
    contract_function = carbon_account.functions.registerUser(user_address)
    receipt = send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
    print(f"User {user_address} registered: {receipt}")

async def link_wallet(user_address, wallet_address):
    contract_function = carbon_account.functions.linkWallet(user_address, wallet_address)
    receipt = send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
    print(f"Wallet {wallet_address} linked to user {user_address}: {receipt}")

async def credit_carbon(user_address, amount):
    contract_function = carbon_account.functions.creditCarbon(user_address, amount)
    receipt = send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
    print(f"Added {amount} carbon credits to {user_address}: {receipt}")

# 2. Fonctionnalités du contrat CarbonPayment
async def pay_for_carbon_credits(to_address, amount):
    eth_amount = web3.toWei(amount, 'ether')  # Exemple : 1 ETH = 1000 crédits
    contract_function = carbon_payment.functions.payForCarbonCredits(to_address, amount)
    receipt = send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY, eth_amount)
    print(f"Paid {eth_amount} ETH for {amount} carbon credits: {receipt}")

async def convert_and_mint(user_address, fiat_amount):
    contract_function = carbon_payment.functions.convertAndMint(user_address, fiat_amount)
    receipt = send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
    print(f"Converted {fiat_amount} fiat to carbon credits for {user_address}: {receipt}")

# 3. Fonctionnalités du contrat CarbonStaking
async def stake_carbon(amount):
    contract_function = carbon_staking.functions.stake(amount)
    receipt = send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
    print(f"Staked {amount} carbon credits: {receipt}")

async def unstake_carbon(amount):
    contract_function = carbon_staking.functions.unstake(amount)
    receipt = send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
    print(f"Unstaked {amount} carbon credits: {receipt}")

# 4. Fonctionnalités du contrat CarbonToken (ERC-20)
async def approve_token(spender_address, amount):
    contract_function = carbon_token.functions.approve(spender_address, amount)
    receipt = send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
    print(f"Approved {spender_address} to spend {amount} tokens: {receipt}")

async def transfer_token(to_address, amount):
    contract_function = carbon_token.functions.transfer(to_address, amount)
    receipt = send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
    print(f"Transferred {amount} tokens to {to_address}: {receipt}")