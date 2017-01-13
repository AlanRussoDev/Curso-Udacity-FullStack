from twilio.rest import TwilioRestClient

account_sid = "ACce222ce91ec08a844cfee432d44fdb16" # Your Account SID from www.twilio.com/console
auth_token  = "31d7860e934f227e6bfa01064c76aef1"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="My name is Alan",
    to="+5511947851617",    # Replace with your phone number
    from_="+55947851617") # Replace with your Twilio number

print(message.sid)
