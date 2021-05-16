from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account1 = "0xBD7DAb35bb6f72C6f853361b794899E56914F60b"
account2 = "0x5987bbB1cd303fE1De47160E4E84aC3d75BE83d4"

private_key1 = "3d86ee0acada218e482f2e4d211a1120b97c01b3f16bd0b6590b4c0df04cb560"

# get nonce
nonce = web3.eth.getTransactionCount(account1)

# build transaction
tx = {
    'nonce': nonce,
    'to': account2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key1)

# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# get transaction hash
print(web3.toHex(tx_hash))