from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://dfujzxbqpvifef:c9608ab1f4ebaf227c53571b7ea2fde71141282ee69299e6158f5d63e2b425b1@ec2-54-243-235-153.compute-1.amazonaws.com:5432/ddi65anbcm45jf')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class Televisor(db.Model):
    __tablename__ = 'televisor'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(80), nullable=False, unique=True)
    clicks = db.Column(db.INTEGER, nullable=False)

class Fridge(db.Model):
    __tablename__ = 'fridge'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(80), nullable=False, unique=True)
    clicks = db.Column(db.INTEGER, nullable=False)


if __name__ == '__main__':
    app.run()