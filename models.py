from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy()

DEFAULT_IMG_URL = 'https://www.top13.net/wp-content/uploads/2015/10/perfectly-timed-cat-photos-funny-cover.jpg'

def connect_db(app):
    """ Connects to database """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    
    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(30), 
                    nullable=False)
    species = db.Column(db.String(30),                              nullable=False)
    photo_url = db.Column(db.String(200), 
                    default=DEFAULT_IMG_URL)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False,
                    default=True)
    