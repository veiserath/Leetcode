def numUniqueEmails(emails):
	
	new_emails = []
	for email in emails:
		email = email.split('@')
		for letter in email[0]:
			if letter == '.':
				email[0] = email[0].replace(letter, '')
			if letter == '+':
				email[0], *temp = email[0].split('+')

		new_emails.append(email[0]+'@'+email[1])
	
	
	return (set(new_emails))

emails = ["test.ema+il+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

print(numUniqueEmails(emails))
