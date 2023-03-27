import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


class NotificationManager:
    @staticmethod
    def send_email(name, email, phone, message):
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=EMAIL,
                    msg=f"Subject:New message\n\nName: {name}\n"
                        f"Email: {email}\nPhone: {phone}\nMessage: {message}".encode('utf-8').strip())
        except smtplib.SMTPException:
            print("Error: unable to send email")

