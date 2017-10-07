from flask import Flask, request, redirect
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+12097134304": "Rutherford Williams",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
}


@app.route("/getinput", methods=['GET', 'POST'])
def hello_monkey():
    # Get the caller's phone number from the incoming Twilio request
    from_number = request.values.get('From', None)
    resp = VoiceResponse()

    # if the caller is someone we know:
    if from_number in callers:
        # Greet the caller by name
        resp.say("Hello " + callers[from_number])
    else:
        resp.say("Hello Monkey")

    return str(resp)
