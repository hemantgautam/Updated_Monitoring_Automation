
from twilio.rest import Client


class WhatsApp:
	def __init__(self):
		self.account_sid = 'ACfd6e5d0b3197be8c89ce9cefeca18baa'
		self.auth_token = 'f2449ff65ebf2a48787b68d3a17c9f2e'
	

	def send_whatsapp_text(self):
		alert_message = "Alert: Ended Not OK Images email has been sent. Please check your gmail"
		client = Client(self.account_sid, self.auth_token)
		message = client.messages.create(
	  		from_='whatsapp:+14155238886',
	  		body=alert_message,
	  		to='whatsapp:+918860348161'
		)
		return message.sid
