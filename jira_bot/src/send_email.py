import smtplib

from email.mime.text import MIMEText

def send_email(filename):
    fp = "Blacklist Proxies\n"
    for line in filename:
        fp+=str(line.replace("\.",".").replace("$",""))
    msg = MIMEText(fp)
    msg['Subject'] = 'SQUID - Blocked URLs'
    msg['From'] = "noreply@example.com"
    msg['To'] = "group@example.com"

    s = smtplib.SMTP('relay.example.com')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
