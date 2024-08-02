import smtplib, ssl
host = "smtp.gmail.com"
port = 465

username = "abdulrasheeds13@gmail.com"
password = "nzjurpkyssdqavgw"

receiver = "abdulrasheeds13@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
how are you today
bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)




