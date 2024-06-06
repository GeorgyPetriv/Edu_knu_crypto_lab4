from src.blockchain import Blockchain
from src.client import Client
from src.scheme import Transaction


blockchain = Blockchain()

alice = Client("Alice", balance=100)
bob = Client("Bob", balance=100)

transactions = [
    alice.makeTransaction(bob, 34),
    bob.makeTransaction(alice, 68),
    bob.makeTransaction(alice, 32),
    alice.makeTransaction(bob, 65)
]

for transaction in transactions:
    print(f'<Transaction: {transaction.sender}> - {transaction.receiver}: {transaction.amount}')
    blockchain.transaction_process(transaction)
    receiver = transaction.receiver
    receiver.receiveTransaction(transaction.amount)

print("\nProof of work")
print("All is OK") if blockchain.chain[1].proof_of_work() else print("Error.")

print("\nBlock stats")
print(blockchain.block_stats(block_position=1))
