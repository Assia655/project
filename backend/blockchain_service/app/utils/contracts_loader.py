import json
from web3 import Web3

def load_contract(web3: Web3, contract_abi_path: str, contract_address: str):
    """
    Charge un contrat intelligent à partir de son ABI et de son adresse.
    
    :param web3: Instance de Web3
    :param contract_abi_path: Chemin vers le fichier JSON contenant l'ABI du contrat
    :param contract_address: Adresse du contrat sur la blockchain
    :return: Instance du contrat
    """
    # Charger l'ABI depuis le fichier
    with open(contract_abi_path, 'r') as abi_file:
        contract_abi = json.load(abi_file)

    # Charger le contrat à l'aide de Web3
    contract = web3.eth.contract(address=web3.toChecksumAddress(contract_address), abi=contract_abi)
    return contract
