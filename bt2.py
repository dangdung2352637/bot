from web3 import Web3

import config
import time

bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))

print(web3.isConnected())

account_1 = "0xFD3A99c87673248651Bff32fbFbf082272E62e31"
account_2 = "0xF8846b5A085Bf7c93B6dd6c8cD485C5A0dFff45b"

balance = web3.eth.get_balance(account_1)
humanReadable = web3.fromWei(balance, "ether")
print(humanReadable)

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce' : nonce,
    "to" : account_2,
    'value' : web3.toWei(0.001, "ether"),
    'gas' : 210000 ,
    'gasPrice' : web3.toWei("5", "gwei")
}

signed_tx = web3.eth.account.signTransaction(tx,"")
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

