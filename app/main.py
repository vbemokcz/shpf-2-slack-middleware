import os
import smtplib

from flask import Flask, request, json

from app.slack_sender import SlackSender


SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL')


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return '<h1><a href="https://github.com/malchikkCZ/shpf-2-slack-middleware">SHPF-2-SLCK MiddleWare</a></h1>'

@app.route('/theme-publish/<auth_hash>', methods=['POST'])
def theme_publish_endpoint(auth_hash):
    if auth_hash == os.environ.get('AUTH_HASH'):
        data = request.json
        theme_id = data['id']
        theme_title = data['name']
        shop_name = request.headers.get('X-Shopify-Shop-Domain')

        SLACK = SlackSender(SLACK_TOKEN, SLACK_CHANNEL)
        SLACK.send(f'New master theme *{theme_title}* id *{theme_id}* has been published at {shop_name}.')

        return 'Success', 200

    return 'Failure', 500

@app.route('/draft_order/<auth_hash>', methods=['POST'])
def draft_order_endpoint(auth_hash):
    if auth_hash == os.environ.get('AUTH_HASH'):
        data = request.json

        with smtplib.SMTP('smtp.gmail.com') as mailserver:
            mailserver.starttls()
            mailserver.login(user=os.environ.get('MAIL_FROM'), password=os.environ.get('MAIL_PASS'))
            mailserver.sendmail(
                from_addr=os.environ.get('MAIL_FROM'),
                to_addrs=os.environ.get('MAIL_TO'),
                msg=f'Subject:Webhook test message\n\n{json.dumps(data)}'
            )

        return 'Success', 200

    return 'Failure', 500