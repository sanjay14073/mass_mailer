# Mass Mailing Queue with Redis and Email Automation

This project is a Python-based mass mailing system that uses a Redis queue to manage the emails to be sent. The script pulls emails from an Excel file and enqueues them for mass mailing, handling email sending via SMTP. Environment variables are used to securely store sensitive information like email credentials.

## Features
- Loads emails from an Excel file.
- Uses Redis to manage a queue for sending emails.
- Sends emails with a simple text body using Gmail's SMTP.
- Secure configuration using environment variables.

## Prerequisites
Before running this project, ensure you have the following:
- Python 3.x installed on your machine.
- A Redis instance running (locally or on the cloud).
- A Gmail account with an app-specific password (if two-factor authentication is enabled).

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repository-url/mass-mailing-queue.git
cd mass-mailing-queue
```

### 2. Install Dependencies
Ensure you have `pip` installed. Install the necessary Python packages by running:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory and add the following environment variables:
```bash
SENDER_MAIL=your_email@gmail.com
SENDER_APP_PASSWORD=your_app_password
REDIS_HOST=your_redis_host
REDIS_PORT=your_redis_port
REDIS_PASSWORD=your_redis_password
```

> **Note**: Do not share your `.env` file publicly, as it contains sensitive information.

### 4. Prepare the Excel File
Create an Excel file named `mail1.xlsx` in the root directory. The file should contain a column named `email` with all the recipient emails.

### 5. Running the Script
Run the script to start processing the Redis queue and sending emails:
```bash
python main.py
```

## How It Works
1. The script loads emails from an Excel file and enqueues them in a Redis queue (`mass_mailing_queue`).
2. A loop runs with a timeout of 2000 seconds, dequeuing emails and sending them using the Gmail SMTP server.
3. If email sending fails, the email is re-enqueued in the Redis queue for retrying.

## Project Structure
```
mass-mailing-queue/
│
├── .env                  # file containing the environment variables
├── main.py               # Main script that sends emails
├── mail_utils.py         # Utility for sending emails via SMTP
├── mail1.xlsx            # Excel file containing recipient emails
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Dependencies
- **pandas**: For handling Excel file operations.
- **redis**: For interfacing with the Redis queue.
- **python-dotenv**: For loading environment variables from a `.env` file.
- **smtplib** (built-in): For sending emails using SMTP.
- **email** (built-in): For composing emails with attachments.

## Notes
- This script currently only handles sending plain text emails.
- Ensure that the `.env` file is correctly configured and never shared publicly.
- You may modify the email subject and body within the script (`send_mail` function in `mail_utils.py`).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
