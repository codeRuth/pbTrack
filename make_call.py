# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
import threading
import time

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC75d65769ec86e0555ae48bc2b245a1b3"
auth_token = "d886780ec3cc9794b69ecfc051e03817"


class Call(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.client = Client(account_sid, auth_token)
        self.number = number

    def make_call(self):
        call = self.client.calls.create(
            to=self.number,
            from_="+12064623728",
            url="https://pbtrack.herokuapp.com/outbound"
        )
        return call

    def run(self):
        self.make_call()


if __name__ == '__main__':
    c = Call("+918660420224")
    c1 = Call("+917411924458")
    c.start()
    c1.start()
    # make_call("+918660420224")
    # make_call("+917411924458")
