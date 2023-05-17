import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = 90000
my_email = "mitultiwari35@gmail.com"
password = "wthawdmpalhhlajt"
URL = "https://www.amazon.in/Weight-Lifting-Power-lifting-Brass-Buckle/dp/B0B62XR9Y4/ref=sr_1_45?crid=R9XZWZ8QT19W&keywords=gym+belt&qid=1678179326&sprefix=gym+bel%2Caps%2C289&sr=8-45"
headers={
   "Accept-Language": "en-US,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price_tag = soup.find("span", class_="a-price-whole").getText().split(",")
price = ""
for i in price_tag:
    if "." in i:
        price += i[0:-1]
    else:
        price += i
price = int(price)

if price<= BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="mitultiwari35@gmail.com", password=password)
        connection.sendmail(from_addr="mitultiwari35@gmail.com", to_addrs="mitultiwari777@gmail.com",
                            msg=f"Subject:Price ALert\n\nThe below product is selling at {price} and price you wanted it at was {BUY_PRICE}\n Buy here: {URL}")