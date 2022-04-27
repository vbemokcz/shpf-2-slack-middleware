from slack_sdk import WebClient


class SlackSender:

    def __init__(self, token, channel):
        self.client = WebClient(token)
        self.channel = channel

    def send(self, message):
        response = self.client.chat_postMessage(
            channel=self.channel,
            text=message
        )
