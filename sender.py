import smtplib

HOST = 'localhost'
PORT = 8080
from_addr = input("From: ")
to_addrs  = input("To: ").split()
subject = input("Subject: ")
print("Enter message, end with ^D:")
# Add the From: and To: headers at the start!
lines = [f"From: {from_addr}", f"To: {', '.join(to_addrs)}", 
         f"Subject: {subject}", ""]
while True:
    try:
        lines.append(input())
    except EOFError:
        break
msg = "\n".join(lines)

print(f"Sending to {HOST}:{PORT}")
with smtplib.SMTP(HOST, PORT) as server:
    server.set_debuglevel(1)
    try:
        refused = server.sendmail(from_addr, to_addrs, msg)
    except smtplib.SMTPException as error:
        print(f"Error: {error}")
    else:
        if refused:
            for recipient, code in refused.items():
                print(f"{code[0]} {code[1]}: {recipient}")
        else:
            print("Sent to all recipients successfully")
