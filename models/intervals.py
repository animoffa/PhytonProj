from extensions import db

class Intervals(db.Model):
    __tablename__ = 'interval'
    id = db.Column(db.Integer, primary_key=True)
    interval = db.Column(db.String(30), unique=True, nullable=False)