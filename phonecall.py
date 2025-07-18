from twilio.rest import Client

# Your Twilio credentials
account_sid = 'ACb81a261f6fb74516aa67604f4d25c8f7'
auth_token = 'aea9fbce44a4c39ca8c64586ae32abcc'
twilio_phone_number = '+16292901335'  # Replace with your Twilio number
to_phone_number = '+917232001202'   # Replace with the verified phone number you want to call

# Create Twilio client
client = Client(account_sid, auth_token)

# Make the call
call = client.calls.create(
    to=to_phone_number,
    from_=twilio_phone_number,
    twiml='<Response><Say>Hello, this is an automated call from Python using Twilio. Have a great day!</Say></Response>'
)

print(f"Call initiated with SID: {call.sid}")
