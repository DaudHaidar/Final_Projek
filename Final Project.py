import stdiomask
import smtplib
from email.mime.text import MIMEText

# connect with Google's servers
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# use username or email to log in
username = input("Email:")
password = stdiomask.getpass()

from_addr = username
alamat_penerima = input("Alamat email penerima:")
to_addrs = []
to_addrs.append(alamat_penerima)

# the email lib has a lot of templates
# for different message formats,
# on our case we will use MIMEText
# to send only text
pesan = input("Tulis Pesan:")
subjek = input("Subjek:")
message = MIMEText(pesan)
message['subject'] = subjek
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)

# we'll connect using SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# to interact with the server, first we log in
# and then we send the message
server.login(username, password)
server.sendmail(from_addr, to_addrs[0], message.as_string())
server.quit()