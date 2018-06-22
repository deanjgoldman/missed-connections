# -*- coding: utf-8 -*-
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
import random
from queries import MissedConnections

app = Flask(__name__)


def get_content(msg):
    # Get content by splitting words into tokens. Iterate through content (post by post),
    # If there is a match, append the post to matches and select from matches, otherwise
    # select randomly from body of posts.
    msg_tokens = msg.lower().split(" ")
    mc = MissedConnections()
    content = mc.content
    matches = []
    for post in content:
        if any(phrase in post.lower() for phrase in msg_tokens):
            matches.append(post)
        else:
            pass
    if len(matches) > 0:
        text = random.choice(matches)
    else: 
        text = random.choice(content)
    return text


@app.route('/sms', methods=['POST', 'GET'])
def sms_reply():
    resp = MessagingResponse()
    text = get_content(request.form["Body"])
    resp.message(text, method='POST')
    return str(resp)


if __name__ == '__main__':
    app.run()
