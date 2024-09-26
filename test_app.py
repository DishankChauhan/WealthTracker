import os
from dotenv import load_dotenv
from bank_connection import get_account_balance
from notification import send_notification

load_dotenv()


def test_bank_connection():
    balance = get_account_balance()
    if balance is not None:
        print(f"Successfully retrieved balance: ₹{balance:.2f}")
    else:
        print("Failed to retrieve balance")


def test_notification(balance):
    send_notification(balance)


def main():
    print("Testing HDFC Account Balance Notifier...")

    # Test bank connection
    print("\nTesting bank connection:")
    test_bank_connection()

    # Test notification
    print("\nTesting notification:")
    test_balance = 10000.00  # Example balance for testing
    test_notification(test_balance)


if __name__ == "__main__":
    main()