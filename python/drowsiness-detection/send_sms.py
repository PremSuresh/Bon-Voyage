from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
def alert():
    client = Client(account_sid, auth_token)

    my_msg = "Your Friend " + my_cell + " is drowsy while driving"

    message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)
    print ( "sms sent")
