from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console

account_sid = ' '

auth_token = ' '

client = Client(account_sid, auth_token)

message = client.messages.create(body='Hello World!', from_='whatsapp:+14155238886', to='whatsapp:+4423029483727')

print(message.sid)