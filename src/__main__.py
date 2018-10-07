import email_wrapper as email
from pathlib import Path
import time

loopmode = False

creds = []
with open(str(Path.home()) + "/.remail/login.conf", "r") as login_conf:
	creds = login_conf.read().split("\n")
	loginconf = ""

while True:
	emails = email.getUnreads(creds)
	
	for mail in emails:
		email.forward(mail, creds)
	
	if not loopmode:
		exit(0)
	time.sleep(30)