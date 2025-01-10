from web3 import Web3

# Configuration de l'URL du nœud Ethereum (RPC endpoint)
ETHEREUM_RPC_URL = "https://sepolia.infura.io/v3/4b8996c62c8a4ea583e48cd3c7a02fb5" 
# Initialisation de Web3
web3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC_URL))

# Vérification de la connexion
if not web3.is_connected():
    raise ConnectionError("Impossible de se connecter au réseau Ethereum")

# Configuration du compte par défaut si nécessaire
web3.eth.default_account = "0xYourDefaultAccount"  # Remplacez par l'adresse par défaut si nécessaire
