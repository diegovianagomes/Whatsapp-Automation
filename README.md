# WhatsApp Automation

This project automates sending WhatsApp messages using the Twilio API.

## How to Use

1. Install the required dependencies:
   ```bash
   pip install twilio python-dotenv schedule
   ```

2. Set up your environment variables in the .env file:
  ```bash
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
```

3. Run the script:
```bash
python3 wpp_exercise_automation.py
```
Scheduling
The script is set up to send messages at specific times using the schedule library. You can modify the schedule in the script to fit your needs.

Important Notes
.env File: Never share your .env file publicly as it contains sensitive information like your Twilio credentials. Add it to .gitignore to avoid accidentally committing it.

PythonAnywhere: If you're running this on PythonAnywhere, ensure the scheduled task is set to the correct UTC time.

Feel free to contribute or customize this project further!
