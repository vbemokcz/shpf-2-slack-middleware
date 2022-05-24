from datetime import datetime, timedelta

from app.main import db


class DraftOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shop = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    order_name = db.Column(db.String(100), nullable=False)

    @classmethod
    def delete_expired(cls):
        limit = datetime.now() - timedelta(days=7)
        cls.query.filter(cls.datetime <= limit).delete()
        db.session.commit()


db.create_all()