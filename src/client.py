from uuid import uuid4
from src.scheme import Transaction


class Client:
    def __init__(self, name: str, balance=50):
        self.id = str(uuid4())
        self.name = name
        self.balance = balance
        self.starting_balance = balance

    def makeTransaction(self, receiver, amount: int):
        if amount > self.balance:
            print(f"Error: negative balance")
            return
        if receiver == self:
            print('Error: sender equals to receiver')
            return
        if amount < 0:
            print(f"Error: negative amount")
            return
        transaction = Transaction(self, receiver, amount)
        self.balance -= amount
        return transaction

    def receiveTransaction(self, amount: int):
        self.balance += amount
