import stdiomask
import smtplib
from email.mime.text import MIMEText

# SUMBER : https://humberto.io/blog/sending-and-receiving-emails-with-python/




# connect with Google's servers
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# use username or email to log in
username = input("Email:")
password = stdiomask.getpass()

from_addr = username
jumlah_penerima = int(input("Jumlah penerima:"))
to_addrs = []
for receiver in range(jumlah_penerima):
   alamat_penerima = input("Alamat email penerima:")
   to_addrs.append(alamat_penerima)


#print(to_addrs)

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
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()