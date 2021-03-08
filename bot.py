import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path= env_path)

SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
SLACK_TOKEN= os.environ['SLACK_TOKEN']

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(
    SLACK_SIGNING_SECRET,'/slack/events',app
)

client = slack.WebClient(token = SLACK_TOKEN)
client.chat_postMessage(channel = '#bot-test-kai', text = "Hello world.")

if __name__ == "__main__":
    app.run(debug = True, port = 80)