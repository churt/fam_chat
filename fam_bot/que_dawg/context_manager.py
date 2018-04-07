import os
from fam_bot.settings import SLACK_TOKEN
from slackclient import SlackClient

class QueBot(object):

    def __init__(self, token=None):
        token = os.environ.get("SLACK_TOKEN")
        if token is None:
            raise KeyError("Must Include Slack Token")
        self.sc = SlackClient(token)

    def handle(self, predicate):
        pass