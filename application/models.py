from application import db, login_manager
from flask_login import UserMixin
#from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    relation = db.relationship('Anime_Watching', backref='user', lazy=True)
    def __repr__(self):
        return ''.join([
            'User: ', self.firstname, ' ', self.lastname, '\r\n',
            'Email: ', self.email
            ])
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    year_released = db.Column(db.String(4), nullable=False)
    relation = db.relationship('Anime_Watching', backref='anime', lazy=True)
    relation2 = db.relationship('Anime_Completed', backref='anime', lazy=True)

    def __repr__(self):
        return ''.join([
            'Title: ', self.title, '\r\n',
            'Year Released: ', self.year_released, '\r\n',
            'Genre: ', self.genre
            ])

class Anime_Watching(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    anime_id = db.Column(db.Integer, db.ForeignKey('anime.id'), nullable=False)
    episode = db.Column(db.Integer, nullable=True)
    #date_started = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return ''.join([
            'Title: ', self.anime_id.title, '\r\n',
            'Episode: ', self.episode, '\r\n'
            #'Date Started: ', self.date_started
            ])

class Anime_Completed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    anime_id = db.Column(db.Integer, db.ForeignKey('anime.id'), nullable=False)
    #date_started = db.Column(db.Datetime nullable=True)
    #date_finished = db.Column(db.DateTime, nullable=True)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return ''.join([
            'Title: ', self.anime_id.title, '\r\n',
            #'Date Started: ', self.date_started, '\r\n',
            'Rating: ', self.rating, '\r\n'
            #'Date Finished: ', self.date_finished, '\r\n'
            ])
