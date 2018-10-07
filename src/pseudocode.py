
emails = email.getUnreads()

for email in email:
	parsed_data = email.parse(email)
	email.forward(parsed_data)
	email.markRead(parsed_data["id"])