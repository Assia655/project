from web3 import Web3
from app.utils.contracts_loader import load_contract
from app.utils.web3_provider import web3
import asyncio

# Charger les contrats intelligents
carbon_account = load_contract(web3, "carbonAccount.json", "0x86cFd7B586f1a2a7eE34791d56Fd397aD15187ed")
carbon_payment = load_contract(web3, "carbonpayment.json", "0xEADacF21b70c3a8FAbE27DcB3A6237a6DE86889b")
carbon_staking = load_contract(web3, "carbonstaking.json", "0x9a19C34E49cBa80d72D1B25DA21831D285E27081")
carbon_token = load_contract(web3, "carbonToken.json", "0x1C26029981dc109eb1EB6F403Ad4AEDFd29E7f34")

# Adresse utilisateur et clé privée (remplacez par des variables sécurisées)
USER_ADDRESS = "0xA09e8aD094a059C12a6227ef8bE5d00527891304"
PRIVATE_KEY = "ea4d8d6348a7cd9240968cbaaa1447197fa82d4f39fbebb512a83a748cab0774"

# Fonction pour signer et envoyer une transaction
async def send_transaction(contract_function, user_address, private_key, value=0):
    try:
        # Construire la transaction
        transaction = contract_function.build_transaction({
            'from': user_address,
            'value': value,  # Montant en Wei
            'gas': 3000000,  # Limite de gaz
            'gasPrice': web3.to_wei('20', 'gwei'),  # Prix du gaz
            'nonce': web3.eth.get_transaction_count(user_address),  # Nonce
        })

        # Signer la transaction
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)

        # Envoyer la transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

        # Attendre la réception
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
        if receipt is None or not receipt['status']:
            raise Exception("Transaction échouée sur la blockchain.")
        return receipt
    except Exception as e:
        raise Exception(f"Erreur lors de la transaction : {str(e)}")

# 1. Fonctionnalités du contrat CarbonAccount
async def register_user(user_address):
    """Appeler la fonction `registerUser` dans le contrat CarbonAccount."""
    try:
        contract_function = carbon_account.functions.registerUser(user_address)
        receipt = await send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
        print(f"Utilisateur {user_address} enregistré avec succès, receipt: {receipt.transactionHash.hex()}")
        return receipt
    except Exception as e:
        print(f"Erreur lors de l'enregistrement de l'utilisateur : {e}")
        raise

async def link_wallet(user_address, wallet_address):
    """Associer un portefeuille à un utilisateur."""
    try:
        contract_function = carbon_account.functions.linkWallet(user_address, wallet_address)
        receipt = await send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
        print(f"Portefeuille {wallet_address} lié à l'utilisateur {user_address} : {receipt.transactionHash.hex()}")
        return receipt
    except Exception as e:
        print(f"Erreur lors de la liaison du portefeuille : {e}")
        raise

async def credit_carbon(user_address, amount):
    """Ajouter des crédits carbone à un utilisateur."""
    try:
        contract_function = carbon_account.functions.creditCarbon(user_address, amount)
        receipt = await send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
        print(f"Ajouté {amount} crédits carbone à {user_address} : {receipt.transactionHash.hex()}")
        return receipt
    except Exception as e:
        print(f"Erreur lors de l'ajout de crédits carbone : {e}")
        raise

# 2. Fonctionnalités du contrat CarbonPayment
async def pay_for_carbon_credits(to_address, amount):
    """Payer des crédits carbone."""
    try:
        eth_amount = web3.to_wei(amount, 'ether')
        contract_function = carbon_payment.functions.payForCarbonCredits(to_address, amount)
        receipt = await send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY, eth_amount)
        print(f"Payé {eth_amount} ETH pour {amount} crédits carbone : {receipt.transactionHash.hex()}")
        return receipt
    except Exception as e:
        print(f"Erreur lors du paiement de crédits carbone : {e}")
        raise

async def convert_and_mint(user_address, fiat_amount):
    """Convertir un montant en fiat et créer des crédits carbone."""
    try:
        contract_function = carbon_payment.functions.convertAndMint(user_address, fiat_amount)
        receipt = await send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
        print(f"Converti {fiat_amount} fiat en crédits carbone pour {user_address} : {receipt.transactionHash.hex()}")
        return receipt
    except Exception as e:
        print(f"Erreur lors de la conversion et de la création : {e}")
        raise

# 3. Fonctionnalités du contrat CarbonStaking
async def stake_carbon(amount):
    """Staker des crédits carbone."""
    try:
        contract_function = carbon_staking.functions.stake(amount)
        receipt = await send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
        print(f"Staké {amount} crédits carbone : {receipt.transactionHash.hex()}")
        return receipt
    except Exception as e:
        print(f"Erreur lors du staking : {e}")
        raise

async def unstake_carbon(amount):
    """Retirer des crédits carbone stakés."""
    try:
        contract_function = carbon_staking.functions.unstake(amount)
        receipt = await send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
        print(f"Retiré {amount} crédits carbone stakés : {receipt.transactionHash.hex()}")
        return receipt
    except Exception as e:
        print(f"Erreur lors du unstaking : {e}")
        raise

# 4. Fonctionnalités du contrat CarbonToken (ERC-20)
async def approve_token(spender_address, amount):
    """Approuver une adresse pour dépenser des tokens."""
    try:
        contract_function = carbon_token.functions.approve(spender_address, amount)
        receipt = await send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
        print(f"Approuvé {spender_address} pour dépenser {amount} tokens : {receipt.transactionHash.hex()}")
        return receipt
    except Exception as e:
        print(f"Erreur lors de l'approbation des tokens : {e}")
        raise

async def transfer_token(to_address, amount):
    """Transférer des tokens ERC-20."""
    try:
        contract_function = carbon_token.functions.transfer(to_address, amount)
        receipt = await send_transaction(contract_function, USER_ADDRESS, PRIVATE_KEY)
        print(f"Transféré {amount} tokens à {to_address} : {receipt.transactionHash.hex()}")
        return receipt
    except Exception as e:
        print(f"Erreur lors du transfert des tokens : {e}")
        raise
