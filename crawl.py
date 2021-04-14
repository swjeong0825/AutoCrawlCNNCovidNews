from bs4 import BeautifulSoup
from urllib.request import urlopen
import smtplib
from datetime import date
import sys
sys.path.append('C:\\Users\\swjeo\\Desktop\\PythonAutomate\\venv\\Lib\\site-packages')



today = str(date.today())
date1 = today[5:] + '-'
date2 = today[2:4]
today = date1 + date2
url = 'https://www.cnn.com/world/live-news/coronavirus-pandemic-vaccine-updates-' + today + '/index.html'
print(url);


with urlopen(url) as response:
    soup = BeautifulSoup(response, 'html.parser')
    h2 = soup.select('h2')
    p = (soup.select('p', class_='Text-sc-1amvtpj-0-p render-stellar-contentstyles__Paragraph-sc-9v7nwy-2 fAchMW'))
    body = str.encode("")

    for index, anchor in enumerate(p):
        if len(anchor) > 2:
            continue

        line = anchor.get_text().encode("utf-8")
        body = body + line
        if len(anchor) == 1:
            body = body + str.encode("\n")
        elif len(anchor) == 0:
            body = body + str.encode("\n") + str.encode("\n")


    body_str = body.decode()



gmail_user = "swjeong0825@gmail.com"

# gmail_pw = "myPassword"

sent_from = "swjeong0825@gmail.com"
to = "jeong723@gmail.com"
# to = "swjeong0825@gmail.com"
subject = "CNN Covid Update"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body_str)

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
server.login(gmail_user, gmail_pw)
server.sendmail(sent_from, to, email_text.encode("utf8"))
server.close()
print ("email sent")



