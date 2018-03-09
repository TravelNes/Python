import os

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'you-guess-key'
SQLALCHEMY_DATABASE_URI = 'mysql://root:yzh199302@localhost:3306/test'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
