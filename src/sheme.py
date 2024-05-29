from uuid import uuid4
from datetime import datetime
import hashlib
import json
from src.hashtree import HashTree


class Transaction:
    def __init__(self, sender, receiver, amount: int):
        self.id = str(uuid4())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __repr__(self):
        return {
            "id": self.id,
            "sender": self.sender.id,
            "receiver": self.receiver.id,
            "amount": self.amount
        }


class Block:
    def __init__(self, transactions: list[Transaction], previous_block=None):
        self.previous_block_hash = previous_block.hash if previous_block else None
        self.timestamp = (datetime.utcnow()).timestamp()
        self.transactions = transactions
        self.nonce = 0
        self.hashtree = HashTree()
        self.fillTree()
        self.hash = self.__hash__()
        print(f'<Block with hash {self.hash} has been created>')

    def __repr__(self):
        return {
            "previous_hash": self.previous_block_hash,
            "transactions": [transaction.__repr__() for transaction in self.transactions],
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }

    def __hash__(self):
        data2hash = None
        if self.hashtree.root:
            data2hash = f"{self.previous_block_hash}{self.nonce}{self.hashtree.root.hash}"
        else:
            data2hash = f"{self.previous_block_hash}{self.nonce}"
        return hashlib.sha256(data2hash.encode()).hexdigest()

    def fillTree(self):
        for transaction in self.transactions:
            self.hashtree.add(json.dumps(transaction.__repr__()))

    def proof_of_work(self, DIFF=4):
        while True:
            if self.hash[:DIFF] == '0' * DIFF:
                return True
            self.nonce += 1
            self.hash = self.__hash__()

    def getBlockData(self, clients_data: dict):
        for transaction in self.transactions:
            for client in [transaction.sender, transaction.receiver]:
                if client.name not in clients_data:
                    clients_data[client.name] = {"current": client.starting_balance,
                                                 "min": client.starting_balance,
                                                 "max": client.starting_balance}

            clients_data[transaction.sender.name]['current'] -= transaction.amount
            clients_data[transaction.receiver.name]['current'] += transaction.amount
            clients_data[transaction.sender.name]['min'] = min(clients_data[transaction.sender.name]['min'],
                                                               clients_data[transaction.sender.name][
                                                                   'current'])
            clients_data[transaction.sender.name]['max'] = max(clients_data[transaction.sender.name]['max'],
                                                               clients_data[transaction.sender.name][
                                                                   'current'])
        return clients_data
