from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio
import geocoder

g = geocoder.ip('me')
c = g.latlng
a = str(c[0])
b = str(c[1])


# Find these values at https://twilio.com/user/account
client = Client(account_sid, auth_token)

my_msg = "Your Friend " + my_cell + " is drowsy while driving at Lat:- " + a + " Long:- " + b

message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
print ( "sms sent")