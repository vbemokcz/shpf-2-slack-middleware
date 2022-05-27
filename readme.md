# SHPF-2-SLCK MiddleWare

Simple flask middleware to convert some shopify webhooks to slack messages.

<br>

### Instalation

Install to your server as any other flask app.
You need to specify following environment variables:

`AUTH_HASH` - any string, works as simple authentication

`SLACK_CHANNEL` - ID of the slack channel, where you want to send messages

`SLACK_TOKEN` - your slack API access token, see slack docs for more information

`DATABASE_URL` - uri of sql database (sqlite or posgresql)