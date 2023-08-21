from music import db

class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, nullable=False)
    artistid = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)

class User(db.Model) :
    userid = db.Column(db.Integer, primary_key=True)
    loginid = db.Column(db.String(50), nullable=False)
    loginpw = db.Column(db.String(50), nullable=False)
    nickname = db.Column(db.String(50), nullable=False)

class Artist(db.Model) :
    artistid = db.Column(db.Integer, primary_key=True)
    artistname = db.Column(db.Text, nullable=False)