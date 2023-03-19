import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"


def get_two_last_closing_price() -> (float, float):
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(url=STOCK_API_ENDPOINT, params=params)
    response.raise_for_status()

    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    yesterday_data = data_list[0]
    before_yesterday_data = data_list[1]
    yesterday_closing_price = float(yesterday_data['5. adjusted close'])
    before_yesterday_closing_price = float(before_yesterday_data['5. adjusted close'])

    return yesterday_closing_price, before_yesterday_closing_price


def calculate_difference_percent(yesterday, before_yesterday) -> float:
    return (yesterday - before_yesterday) / before_yesterday


def get_news():
    params = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(url=NEWS_API_ENDPOINT, params=params)
    response.raise_for_status()

    return response.json()["articles"]


def send_message(text: str):
    client = Client(ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=text,
        from_="+15673392760",
        to="+84365896447"
    )
    print(f"### {message.sid}")


y_val, by_val = get_two_last_closing_price()
diff_percent = calculate_difference_percent(y_val, by_val)

up_down = '🔺' if diff_percent >= 0 else '🔻'

if abs(diff_percent * 100) > 5:
    news = get_news()
    three_articles = news[:3]
    messages = [f"{STOCK}: {up_down}{round(abs(diff_percent * 100))}%\n" \
                f"Headline: {article['title']}\nBrief: {article['description']}"
                for article in three_articles]

    for message_text in messages:
        send_message(message_text)
