# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC75d65769ec86e0555ae48bc2b245a1b3"
auth_token = "d886780ec3cc9794b69ecfc051e03817"
client = Client(account_sid, auth_token)


def make_call(number):
    call = client.calls.create(
        to=number,
        from_="+12064623728 ",
        url="https://pbtrack.herokuapp.com/outbound"
    )
    return call


if __name__ == '__main__':
    make_call("+918660420224")
