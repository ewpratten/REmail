import smtplib

import imaplib
import email
from bs4 import BeautifulSoup

def getUnreads(creds):
	mail=imaplib.IMAP4_SSL('imap.gmail.com',993)
	mail.login(creds[0],creds[1])
	mail.list()
	mail.select()
	typ,data=mail.search(None,'UNSEEN')
	maildata = data
	
	output = []
	for num in data[0].split():
		status, data = mail.fetch(num, '(RFC822)')
		msg = email.message_from_bytes(data[0][1])
		subj = email.header.make_header(email.header.decode_header(msg['Subject']))
		
		# soup body
		soup = BeautifulSoup(str(msg), features="html.parser")
		body = soup.find("div", dir="ltr")
		
		frm = email.header.make_header(email.header.decode_header(msg['From']))
		output.append([num, [str(frm).split("<")[0][:-1], str(frm).split("<")[1][:-1]], str(subj), str(body)])
		mail.store(num,'+FLAGS', 'UNSEEN')
	
	mail.close()
	mail.logout()
	return output

def send_email(creds, recipient, subject, body):
    import smtplib

    FROM = creds[0]
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(creds[0], creds[1])
        server.sendmail(FROM, TO, message)
        server.close()
        print("Success")
    except:
    	print("Fail")

def forward(mail, creds):
	mail[3] = mail[3][15:]
	mail[3] = mail[3][:-6]
	
	if mail[3][0] == ":":
		parsed_body = str(str(mail[3])[1:]).split(":") #Extra safe
		forward_addr = str(parsed_body[0]) + "@" + str(parsed_body[1]) + "." + str(parsed_body[2])
		
		body = str(parsed_body[len(parsed_body) - 1])
		print([forward_addr, body])
		send_email(creds, forward_addr, mail[2], body)
	elif mail[3] == "ping":
		send_email(creds, mail[1][1], mail[2], "pong")
	else:
		send_email(creds, mail[1][1], "REmail server error", "The email you sent did not contain instructions on where to forward it too. Please take a look at: https://github.com/Ewpratten/REmail/blob/master/README.md for details.")