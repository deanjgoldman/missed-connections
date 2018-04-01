# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
import random
from content import MissedConnections

app = Flask(__name__)


def get_content(msg):
    print(msg)
    msg_tokens = msg.lower().split(" ")
    missed_connections = MissedConnections()
    content = missed_connections.content()
    matches = []
    for line in content:
        if any(phrase in line.lower() for phrase in msg_tokens):
            matches.append(line)
        else:
            pass
    if len(matches) > 1:
        text = random.choice(matches)
    else: 
        text = random.choice(content)
    return text


@app.route('/sms', methods=['POST', 'GET'])
def sms_reply():
    resp = MessagingResponse()
    text = get_content(request.form["Body"])
    resp.message(text, method='POST')
    print(resp)
    return str(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
