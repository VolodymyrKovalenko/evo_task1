from flask import Flask, render_template,jsonify, request
from flask_sqlalchemy import SQLAlchemy
from SQLAlchemy_db import Fridge, Televisor
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import os

app = Flask(__name__)
app.secret_key = 'super secret key'
# app.config.from_pyfile('config.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql-vertical-91489')
db = SQLAlchemy(app)


@app.route('/')
def start_page():
    fridges = db.session.query(Fridge)
    televisors = db.session.query(Televisor)
    return render_template('index.html',fridges=fridges, televisors=televisors)


@app.route('/add_click', methods=['POST'])
def add_click():
    obj_type = None
    if request.form.get('type') == 'televisor':
        obj_type = Televisor
    elif request.form.get('type') == 'fridge':
        obj_type = Fridge
    update_obj = UpdateQuery(obj_type,request.form.get('id'))
    return jsonify({"clicks": update_obj.clicks_counter})

class UpdateQuery():
    def __init__(self,type,obj_id):
        self.type = type
        self.obj_id = obj_id

    @property
    def clicks_counter(self):
        query_object = db.session.query(self.type).filter(self.type.id == self.obj_id).first()
        query_object.clicks += 1
        db.session.commit()
        return query_object.clicks

admin = Admin(app)
admin.add_view(ModelView(Fridge, db.session))
admin.add_view(ModelView(Televisor, db.session))

if __name__ == '__main__':
    app.run()
