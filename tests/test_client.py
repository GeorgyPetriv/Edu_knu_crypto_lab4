from unittest import TestCase
from unittest.mock import patch
from src.client import Client


class TestClient(TestCase):
    def test_create_client(self):
        test_client = Client('test_client_name', 100)

        self.assertIsNotNone(test_client.id)
        self.assertIsInstance(test_client, Client)
        self.assertEqual('test_client_name', test_client.name)
        self.assertEqual(100, test_client.balance)
        self.assertEqual(100, test_client.starting_balance)

    def test_make_transaction(self):
        test_client1 = Client('test_client_name1', 100)
        test_client2 = Client('test_client_name1', 200)

        test_transaction = test_client1.makeTransaction(test_client2, 50)

        self.assertEqual(50, test_transaction.amount)
        self.assertEqual(test_client1.id, test_transaction.sender.id)
        self.assertEqual(test_client2.id, test_transaction.receiver.id)

    def test_make_invalid_transaction(self):
        test_client1 = Client('test_client_name1', 100)
        test_client2 = Client('test_client_name2', 100)

        with patch('builtins.print') as mock_print:
            test_client1.makeTransaction(test_client1, 50)
            mock_print.assert_called_with('Error: sender equals to receiver')

        with patch('builtins.print') as mock_print:
            test_client1.makeTransaction(test_client2, 150)
            mock_print.assert_called_with('Error: negative balance')

        with patch('builtins.print') as mock_print:
            test_client1.makeTransaction(test_client2, -150)
            mock_print.assert_called_with('Error: negative amount')