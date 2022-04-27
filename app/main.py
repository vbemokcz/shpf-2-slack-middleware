import os

from flask import Flask, request

from app.slack_sender import SlackSender


SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL')


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'SHPF-2-SLCK MiddleWare'

@app.route('/theme-publish/<str:auth_hash>', methods=['POST'])
def theme_publish_endpoint(auth_hash):
    if auth_hash == os.environ.get('AUTH_HASH'):
        data = request.json
        theme_id = data['id']
        theme_title = data['name']
        shop_name = request.headers.get('X-Shopify-Shop-Domain')

        SLACK = SlackSender(SLACK_TOKEN, SLACK_CHANNEL)
        SLACK.send(f'New master theme **{theme_title}** id **{theme_id}** has been published at {shop_name}.')

        return 'Success', 200

    return 'Failure', 500
