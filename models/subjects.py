from extensions import db

class Subj(db.Model):
    __tablename__ = 'subject'
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(30), unique=True, nullable=False)