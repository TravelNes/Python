from app import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'useexisting': True}

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    username = db.Column(db.String(28), unique=True)
    email = db.Column(db.String(128))
    password = db.Column(db.String(28))
