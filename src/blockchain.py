from src.scheme import Block, Transaction
from src.hashtree import HashTree
import json


class Blockchain:
    def __init__(self, difficulty=4, mxt=3):
        self.difficulty = difficulty
        self.max_transaction_num = mxt

        self.chain: list[Block] = []
        self.transactions: list[Transaction] = []
        self.hashTree: HashTree = HashTree()
        self.block_process()

    def block_process(self, block: Block = None):
        if len(self.chain) == 0:
            block = Block([])  # genesis

        block.proof_of_work(self.difficulty)
        self.chain.append(block)
        self.hashTree.add(block.hash)

    def blockchain_root_hash(self):
        tree = HashTree()
        for block in self.chain:
            tree.add(block.hash)
        return tree.root.hash

    def validation(self):
        if self.blockchain_root_hash() != self.hashTree.root.hash:
            print("Invalid root hashes")
            return False
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if ((current_block.__hash__() != current_block.hash)
                    or (current_block.previous_block_hash != previous_block.hash)):
                print("Invalid block hash")
                return False
        return True

    def transaction_process(self, transaction: Transaction):
        self.transactions.append(transaction)
        if len(self.transactions) >= self.max_transaction_num:
            block = Block(self.transactions, self.chain[-1])
            self.block_process(block)
            self.transactions = []

    def block_stats(self, block_position):
        if block_position >= len(self.chain):
            print('Block position out of range')
            return

        client_balances = {}
        for i in range(block_position+1):
            client_balances = self.chain[i].getBlockData(client_balances)

        return client_balances


def save_to_json(blockchain: Blockchain, default_path='blockchain.json'):
    print('Saving to json')
    with open(default_path, 'w') as f:
        json.dump([block.__repr__() for block in blockchain.chain], f, indent=4)
