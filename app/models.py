from app.main import db


class DraftOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.String(100), nullable=False)
    order_name = db.Column(db.String(100), nullable=False)


db.create_all()