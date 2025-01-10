import os
from web3 import Web3

def load_contract(web3: Web3, abi_filename: str, contract_address: str):
    # Utiliser le chemin correct pour contracts_abi dans app/
    contract_abi_path = os.path.join(os.path.dirname(__file__), "../contrats_abi", abi_filename)
    try:
        with open(contract_abi_path, 'r') as abi_file:
            abi = abi_file.read()
            return web3.eth.contract(address=contract_address, abi=abi)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"ABI file not found: {contract_abi_path}") from e
