from twilio.rest import TwilioRestClient

account_sid = "ACce7913ddf6512a4e65c5cf59b673bf24" # Your Account SID from www.twilio.com/console
auth_token  = "4c0f1d13373479061b5692c61578f030"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Python",
    to="+19186309537",    # Replace with your phone number
    from_="+19187704308") # Replace with your Twilio number

print(message.sid)