import os
from datetime import datetime

import requests
import json
from dotenv import load_dotenv

load_dotenv()


class HDFCBankAPI:
    BASE_URL = "https://api-uat.hdfcbank.com"#is is a placeholder URL

    def __init__(self):
        self.api_key = os.getenv('HDFC_API_KEY')
        self.account_number = os.getenv('HDFC_ACCOUNT_NUMBER')
        self.mobile_number = os.getenv('HDFC_MOBILE_NUMBER')

    def get_account_balance(self):
        url = f"{self.BASE_URL}/API/AA_FetchFinancialInfo"
        headers = {
            "Authorization": f"ApiKey {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "sessionContext": {
                "bankCode": "08",
                "channel": "FIP",
                "userId": "DevUser01",
                "transactionBranch": "089999",
                "externalReferenceNo": "FIPFETC" + datetime.now().strftime("%d%m%Y"),
                "transactingPartyCode": self.mobile_number
            },
            "FetchFinancialInformationRequestDTO": {
                "financialInformationType": "DEPOSIT",
                "dob": "",
                "pan": "",
                "statementStartDate": "",
                "statementEndDate": "",
                "mobileNumber": self.mobile_number,
                "accountNumber": self.account_number,
                "accountReferenceNumber": [
                    "1234678901234567890"  # This might need to be dynamically generated or obtained
                ],
                "informationType": "1",
                "customerID": ""
            }
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            # The structure of the response JSON may vary. Adjust the following line accordingly.
            return response.json().get('balance', None)
        else:
            raise Exception(f"Failed to retrieve account balance. Status code: {response.status_code}")


def get_account_balance():
    try:
        hdfc_api = HDFCBankAPI()
        return hdfc_api.get_account_balance()
    except Exception as e:
        print(f"Error getting account balance: {e}")
        return None