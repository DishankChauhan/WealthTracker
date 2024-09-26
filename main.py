import schedule
import time
import sys
from bank_connection import get_account_balance
from notification import send_notification

def check_and_notify():
    balance = get_account_balance()
    if balance is not None:
        send_notification(balance)
    else:
        print("Failed to retrieve account balance")

def main(test_mode=False):
    if test_mode:
        print("Running in test mode...")
        check_and_notify()
    else:
        print("Starting HDFC Account Balance Notifier with Twilio...")
        schedule.every().day.at("08:00").do(check_and_notify)
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    test_mode = len(sys.argv) > 1 and sys.argv[1] == '--test'
    main(test_mode)