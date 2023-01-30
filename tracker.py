import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL="https://www.jumia.com.tn/adata-flash-disque-uv250-64-go-cle-usb-2.0-silver-458381.html"
headers={"user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0'}
sender_mail='azizjouini906@gmail.com'
sender_pass='zmryjqrkxvsuxtsn'

page=requests.get(URL,headers=headers)

soup=BeautifulSoup(page.content,'html.parser')

def check_price():
    title=soup.find_all("h1", {"class": "-fs20 -pts -pbxs"})[0].get_text().strip()
    price=float(soup.find_all("span",{"class":"-b -ltr -tal -fs24","dir":"ltr"})[0].get_text().split(" ")[0])
    print(price)
    if price<=25:
        send_email()

    


def send_email():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_mail,sender_pass)
    subject='discount jumia'
   
    body=URL

    message="subject: "+subject+" \n\n "+body    

    server.sendmail(
        sender_mail,
        sender_mail,
        message
    )
    server.quit()
    print('email sent!')

while(True):
    check_price()
    time.sleep(60*60*24*7)