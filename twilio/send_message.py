from twilio.rest import Client

account_sid = "AC05ced267afc01bff87f607107dff412c"
auth_token = "f0513bb0d69a01dfcc624cf478695f17"

client = Client(account_sid, auth_token)

client.messages.create(
  to="+5585999399458",
  from_="+14158554728",
  body="Hi Victor, How are you doing?")

print message.sid
