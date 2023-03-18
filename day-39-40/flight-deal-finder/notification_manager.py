import smtplib
from pprint import pprint


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, email, password):
        self.my_email = email
        self.my_password = password

    def send_sms(self, message):
        pprint(message)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(self.my_email, self.my_password)
            for email in emails:
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
