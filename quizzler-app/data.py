import requests

params = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=params)
response.raise_for_status()

data = response.json()

if data["response_code"] == 0:
    question_data = data["results"]

# print(question_data)
