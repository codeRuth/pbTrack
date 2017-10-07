from __future__ import with_statement  # Only necessary for Python 2.5
from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse, Gather
import database

app = Flask(__name__)

# callers = {
#     "+14158675309": "Curious George",
#     "+14158675310": "Boots",
#     "+14158675311": "Virgil",
#     "+14158675312": "Marcel"
# }


@app.route("/outbound", methods=['GET', 'POST'])
def hello_user():
    from_number = request.values.get('To', None)
    print type(from_number)
    resp = VoiceResponse()
    for x in database.get_users():
        if str(x['phone']) == str(from_number):
            resp.say("Hello " + str(x['name']))
    resp.say("Are you available for the delivery today ?")

    # handle the yes or no command
    #
    g = Gather(numDigits=1, action="/handle-yn", timeout=1, method="POST",)
    g.say("If Yes, Press 1, if No Press 2.")

    #
    # resp.say("Thanks for Your Response, Keep shopping with Shopping with us.")
    #
    # # Play an mp3
    # # resp.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
    #
    # # Say a command, and listen for the caller to press a key. When they press
    # # a key, redirect them to /handle-key.
    # g = Gather(numDigits=1, action="/handle-key", method="POST")
    # g.say("To speak to a real monkey, press 1. Press any other key to start over.")
    resp.append(g)

    return str(resp)


@app.route("/handle-yn", methods=['GET', 'POST'])
def handle_yn():
    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)

    if digit_pressed == "1":
        resp = VoiceResponse()
        resp.say("You have said Yes")
        g = Gather(numDigits=1, action="/handle-time", method="POST")
        g.say("Press 1 for 8 AM to 12 PM, Press 1 for 12 AM to 4 PM, Press 1 for 4 AM to 8 PM")
        resp.append(g)
        return str(resp)

    elif digit_pressed == "2":
        resp = VoiceResponse()
        resp.say("You have said No, Gaanduuuuuuuu, pakistan maaa ki bhosda")
        return str(resp)

    # If the caller pressed anything but 1, redirect them to the homepage.
    else:
        return redirect("/")


@app.route("/handle-time", methods=['GET', 'POST'])
def handle_time():
    # Get the digit pressed by the user
    digit_pressed = request.values.get('Digits', None)

    if digit_pressed == "1":
        # 8 AM to 12 PM
        resp = VoiceResponse()
        # resp.dial("+13105551212")
        resp.say("The call failed, or the remote party hung up. Goodbye.")
        return str(resp)

    elif digit_pressed == "2":
        # 12 AM to 4 PM.
        resp = VoiceResponse()
        # resp.dial("+13105551212")
        resp.say("The call failed, or the remote party hung up. Goodbye.")
        return str(resp)

    elif digit_pressed == "3":

        # 4 AM to 8 PM.
        resp = VoiceResponse()
        # resp.dial("+13105551212")
        resp.say("The call failed, or the remote party hung up. Goodbye.")
        return str(resp)

    # If the caller pressed anything but 1, redirect them to the homepage.
    else:
        return redirect("/")
