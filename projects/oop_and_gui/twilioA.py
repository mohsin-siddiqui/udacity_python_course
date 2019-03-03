from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC8b484258ed33bfb2bed58a91482eaf53"
# Your Auth Token from twilio.com/console
auth_token = "95f5dd33b600a96e00658978aad4ae5b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+9779862150545",
    from_="+14698286761",
    body="just checking 3!!!")

print(message.sid)
