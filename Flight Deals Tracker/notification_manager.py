from twilio.rest import Client
import smtplib

password = "***********" #email authorization password here
account_sid = "************************" #twilio account id
auth_token = "***********************" #twilio account password


class NotificationManager:
    def send_alert(self, city_name:str, price:str, date:str):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Alert!\nTicket for {city_name}\nAt lowest price of {price} Euros\nOn {date}\nHurry-up and book now",
            from_="+16076899597",
            to="+918989000595"
        )
        print(message.sid)

    def send_mail(self, city_name:str, price:str, date:str):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="mitultiwari35@gmail.com", password=password)
            connection.sendmail(from_addr="mitultiwari35@gmail.com", to_addrs="mitultiwari777@gmail.com",
                                msg="Subject:Cheap Tickers\n\n"
                                    f"Alert!\nTicket for {city_name}\nAt lowest price of {price} Euros\nOn {date}\nHurry-up and book now")

