from . import db

class Encounter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16))
    iniGiven =db.Column(db.Boolean())
    #entities = db.C


class Entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    maxHp = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    #str = db.Column(db.Tuple)
    #dex = db.Column(db.Tuple)
    #con = db.Column(db.Tuple)
    #wis = db.Column(db.Tuple)
    #int = db.Column(db.Tuple)
    #cha = db.Column(db.Tuple)