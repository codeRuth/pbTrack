from __future__ import with_statement  # Only necessary for Python 2.5
from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse, Gather
import database
import json

app = Flask(__name__)

# callers = {
#     "+14158675309": "Curious George",
#     "+14158675310": "Boots",
#     "+14158675311": "Virgil",
#     "+14158675312": "Marcel"
# }

from_number = None

@app.route("/outbound", methods=['GET', 'POST'])
def hello_user():
    global from_number
    from_number = request.values.get('To', None)
    print type(from_number)
    resp = VoiceResponse()
    for x in database.get_users():
        if str(x['phone']) == str(from_number):
            resp.say("Hello " + str(x['name']), voice='alice')
    resp.say("Are you available for the delivery today ?", voice='alice')
    g = Gather(numDigits=1, action="/handle-yn", timeout=2, method="POST",)
    g.say("If Yes, Press 1, if No Press 2.", voice='alice')
    resp.append(g)

    return str(resp)


@app.route("/handle-yn", methods=['GET', 'POST'])
def handle_yn():
    digit_pressed = request.values.get('Digits', None)

    if digit_pressed == "1":
        resp = VoiceResponse()
        resp.say("You have said Yes", voice='alice')
        return str(resp)

    elif digit_pressed == "2":
        resp = VoiceResponse()
        resp.say("You have said No.", voice='alice')

        g = Gather(numDigits=1, action="/handle-time", method="POST")
        g.say("Press 1 for 8 AM to 12 PM, Press 2 for 12 PM to 4 PM, Press 3 for 4 PM to 8 PM", voice='alice')
        resp.append(g)

        return str(resp)
    # If the caller pressed anything but 1, redirect them to the homepage.
    else:
        return redirect("/")


@app.route("/handle-time", methods=['GET', 'POST'])
def handle_time():
    digit_pressed = request.values.get('Digits', None)

    if digit_pressed == "1":
        resp = VoiceResponse()
        resp.say("8 AM to 12 PM", voice='alice')

        args = {
            'yes': 'False',
            "no": 'True',
            'del_time': '8 AM to 12 PM',
            "pno": str(from_number)
        }

        resp.say("Thanks", voice='alice')

        database.update(json.dumps(args))
        return str(resp)

    elif digit_pressed == "2":
        # 12 AM to 4 PM.
        resp = VoiceResponse()
        resp.say("12 PM to 4 PM", voice='alice')

        args = {
            'yes': 'False',
            "no": 'True',
            'del_time': '12 PM to 4 PM',
            "pno": str(from_number)
        }

        resp.say("Thanks", voice='alice')

        database.update(json.dumps(args))
        return str(resp)

    elif digit_pressed == "3":
        # 4 AM to 8 PM.
        resp = VoiceResponse()
        resp.say("4 PM to 8 PM", voice='alice')

        args = {
            'yes': 'False',
            "no": 'True',
            'del_time': '4 PM to 8 PM',
            "pno": str(from_number)
        }

        resp.say("Thanks", voice='alice')

        database.update(json.dumps(args))
        return str(resp)

    else:
        return redirect("/")
