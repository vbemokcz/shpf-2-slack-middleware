import os
import datetime as dt
import pytz

from flask import request

from app.main import app, db
from app.models import DraftOrder
from app.slack_sender import SlackSender


SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
SLACK_CHANNEL = os.environ.get('SLACK_CHANNEL')


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


@app.route('/draft-order/<shop_name>', methods=['GET'])
def draft_order_get_endpoint(shop_name):

    draft_order = DraftOrder.query.filter_by(shop=shop_name)[-1]

    if draft_order:
        current_time = dt.datetime.now(pytz.timezone('Europe/Berlin'))
        order_time = dt.datetime.strptime(draft_order.created_at.split('+')[0], '%Y-%m-%dT%H:%M:%S')
        order_time = order_time.astimezone()

        print(current_time.strftime('%Y-%m-%d %H:%M'))
        print(order_time.strftime('%Y-%m-%d %H:%M'))

        delta_time = current_time - order_time

        return f'{delta_time.total_seconds()}', 200

    return 'Not found', 404


@app.route('/draft-order/<auth_hash>', methods=['POST'])
def draft_order_post_endpoint(auth_hash):
    if auth_hash == os.environ.get('AUTH_HASH'):
        data = request.json

        draft_order = DraftOrder(
            shop = request.headers.get('X-Shopify-Shop-Domain'),
            created_at = data['created_at'],
            order_name = data['name']
        )

        db.session.add(draft_order)
        db.session.commit()
        return 'Success', 200

    return 'Failure', 500
