from twilio.rest import Client
import threading
import config


class Call(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.client = Client(config.account_sid, config.auth_token)
        self.number = number

    def make_call(self):
        call = self.client.calls.create(
            to=self.number,
            from_= config.TWILIO_NUMBER,
            url="https://pbtrack.herokuapp.com/outbound"
        )
        return call

    def run(self):
        self.make_call()


if __name__ == '__main__':
    c = Call("+918660420224")
    c1 = Call("+917411924458")
    c2 = Call("+919686832383")
    c.start()
    c1.start()
    c2.start()
