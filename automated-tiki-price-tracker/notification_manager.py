import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


class NotificationManager:

    def __init__(self, track_requests):
        self.track_requests = track_requests

    @staticmethod
    def get_product(url: str) -> (str, float):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "Accept-Language": "en,vi;q=0.9"
        }
        response = requests.get(
            url=url,
            headers=headers)
        response.raise_for_status()

        html = response.text

        soup = BeautifulSoup(html, "html.parser")

        title_tag = soup.select_one(".header h1.title")
        price_tag = soup.select_one('.product-price__current-price')
        title = title_tag.get_text()
        price = float(price_tag.get_text().split(" ")[0].replace(".", "").replace('₫', "").strip())

        return title, price

    def send_notification(self):
        for req in self.track_requests:
            email, url, desire_price = req["email"], req["url"], req["price"]
            product_title, current_price = self.get_product(url)
            if current_price <= desire_price:
                message = f"Subject:TIKI PRICE ALERT 🛍️️️️🛍️️️️🛍️️️\n\n{product_title} is now {current_price}₫.\nSee: {url}"
                print(message)
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=EMAIL, password=PASSWORD)
                    connection.sendmail(from_addr=EMAIL, to_addrs=email, msg=message.encode('utf-8'))



