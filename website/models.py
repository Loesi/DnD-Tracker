from . import db

class Encounter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))