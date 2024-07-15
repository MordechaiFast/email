import smtplib
from email.message import EmailMessage


from_addr = input("From: ")
to_addrs  = input("To: ").split()
subject = input("Subject: ")
print("Enter message, end with ^D:")
body = ''
while True:
    try:
        line = input()
    except EOFError:
        break
    body += line + '\n'
msg = EmailMessage()
msg['From'] = from_addr
msg['To'] = to_addrs
msg['Subject'] = subject
msg.set_content(body)

print("Sending")
with smtplib.SMTP('localhost', 8025) as server:
    server.set_debuglevel(1)
    server.send_message(msg)
