import os
import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL= os.environ.get(MY_EMAIL)
PASSWORD = os.environ.get(PASSWORD)

now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")
new_data = data.to_dict("records")

for i in range(len(new_data)):
    if new_data[i]["Day"] == day and new_data[i]["Month"] == month:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", mode="r") as letter_file:
            letter_content = letter_file.read()
            new_letter = letter_content.replace("[NAME]", new_data[i]["Name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=new_data[i]["Email"],
                msg=f"Subject:Happy birthday\n\n{new_letter}"
            )
