from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
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