# Balance Notifier

A Python application that fetches your bank account balance and sends daily notifications to your phone using Twilio. This project is built to help users stay updated on their account balance without needing to log in to their bank accounts manually.

## Features

- Automatically fetches account balance from the bank API (e.g., Setu API or other supported APIs)
- Sends daily SMS notifications with your balance to your phone via Twilio
- Configurable notification time (set to morning by default)
- Secure storage of sensitive API keys using environment variables

## Tech Stack

- **Python**: Core programming language used for development
- **Twilio API**: For sending SMS notifications to the user's phone
- **Setu API** (or HDFC, IDBI Bank API): For fetching bank account balance securely
- **APScheduler**: For scheduling notifications on a daily basis
- **dotenv**: For managing environment variables

## Installation

### Prerequisites

- Python 3.8+
- A Twilio account with a valid phone number
- A Setu (or other bank) API key for fetching bank balance

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/balance_notifier.git
cd balance_notifier
