import datetime as dt
import smtplib
import pandas
import random
import os
from dotenv import load_dotenv

load_dotenv()
MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# 1. Update the birthdays.csv
birthdays_df = pandas.read_csv("birthdays.csv")


# 2. Check if today matches a birthday in the birthdays.csv
def is_birthday(month, day):
    now = dt.datetime.now()
    return now.month == month and now.day == day


def today_birthday():
    return [(row["name"], row["email"]) for (index, row) in birthdays_df.iterrows() if is_birthday(row.month, row.day)]


# 3. If step 2 is true,
# pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
letter_templates = []
directory = "letter_templates"

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        with open(f, "r") as data_file:
            letter_templates += [data_file.read()]

# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    today_birthdays = today_birthday()
    for name, email in today_birthdays:
        letter = random.choice(letter_templates).replace("[NAME]", name).replace("Angela", "Quoc Viet Tran")
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=email,
                            msg=f"Subject:HAPPY BIRTHDAY 🎂🎂🎂\n\n{letter}".encode('utf-8'))

