
import argparse
import requests
from web3 import Web3
from .chains import supported_chains


def get_creation_transaction_hash(endpoint, safe_address, api_key):
    # Setup and send API
    module = 'contract'
    action = 'getcontractcreation'
    params = {'module': module, 'action': action,
              'contractaddresses': safe_address, 'apikey': api_key}
    response = requests.get(endpoint, params=params)
    data = response.json()

    # Parse response
    if response.status_code != 200 or data['status'] != '1':
        raise Exception('API request failed with status code: ',
                        response.status_code)
    return data['result'][0]["txHash"]


def send_creation_transaction_to_dst_chain(private_key, dst_chain, tx):
   # Send to dst chain
    w3 = Web3(Web3.HTTPProvider(dst_chain["rpc"]))
    sender = w3.eth.account.from_key(private_key).address
    receiver = w3.to_checksum_address(dst_chain["proxy_factory"])

    # Set transaction data
    transaction = {
        'to': receiver,
        'gas': int(tx.gas * 1.5),
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(sender),
        'data': tx.input
    }

    # sign transaction data and send transaction
    signed_tx = w3.eth.account.sign_transaction(
        transaction, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print('Transaction sent on %s: %s' % (dst_chain["network"], tx_hash.hex()))


def main():  # pragma: no cover
    """
    The main function executes on commands:
    `python -m gnosis_safe_multichain_deployer` and `$ gnosis_safe_multichain_deployer `.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--src-chain-id', type=int, help='source chain ID')
    parser.add_argument('--dst-chain-id', type=int,
                        help='destination chain ID')
    parser.add_argument('--address', type=str, help='wallet address')
    parser.add_argument('--api-key', type=str, help='api key of etherscan')
    parser.add_argument('--private-key', type=str,
                        help='private key for signing transactions')
    args = parser.parse_args()

    src_chain_id = args.src_chain_id
    dst_chain_id = args.dst_chain_id
    safe_address = args.address
    api_key = args.api_key
    private_key = args.private_key

    src_chain = supported_chains[src_chain_id]
    dst_chain = supported_chains[dst_chain_id]
    w3 = Web3(Web3.HTTPProvider(src_chain["rpc"]))

    # Get safe vault creation data
    creation_txhash = get_creation_transaction_hash(
        src_chain["etherscan_endpoint"], safe_address, api_key)
    tx = w3.eth.get_transaction(creation_txhash)

    # Check factory address
    tx_to = tx.to.lower()
    if tx_to != src_chain["proxy_factory"].lower():
        raise Exception('Wrong factory address form src chain')

    if tx_to != dst_chain["proxy_factory"].lower():
        raise Exception('Wrong factory address form dst chain')

    # Send to dst chain
    send_creation_transaction_to_dst_chain(private_key, dst_chain, tx)
