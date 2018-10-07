import email_wrapper as email
from pathlib import Path

creds = []
with open(str(Path.home()) + "/.remail/login.conf", "r") as login_conf:
	creds = login_conf.read().split("\n")
	loginconf = ""

emails = email.getUnreads(creds)

for mail in emails:
	email.forward(mail, creds)