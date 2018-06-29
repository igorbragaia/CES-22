# -*- coding: utf-8 -*-
import psycopg2, json
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
from flask import render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response, redirect, request, abort, url_for, flash
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)


app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)


# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# silly user model
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = id
        self.password = id


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if Usuario.query.filter_by(username=username, password=password).first() != None:
			id = username
			user = User(id)
			login_user(user)
			return redirect(url_for('index'))
		else:
			return abort(401)
	else:
		return Response(render_template('login.html'))


# somewhere to logout
@app.route("/logout", methods=["GET","POST"])
@login_required
def logout():
    logout_user()
    flash('usuario deslogado')
    return redirect(url_for('index'))


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    flash('usuario ou senha incorretos')
    return Response(render_template('login.html'))


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)


@app.route('/')
@login_required
def index():
    return render_template('index.html', usuario=current_user.name)


@app.route('/cadastrar', methods=["POST"])
def cadastrar():
	try:
		username = request.form['username']
		password = request.form['password']

		if len(list(Usuario.query.filter_by(username=username))) == 0:
			new_user = Usuario(username, password)

			db.session.add(new_user)
			db.session.commit()
			flash('Usuário registrado no banco de dados!')
		else:
			flash('Já existe um usuário com esse nome registrado :(')
	except Exception as e:
		flash('ocorreu o seguinte erro: ', e)
	return redirect(url_for('index'))



class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(2000), unique=True, nullable=False)

    def __init__(self, username, password):
    	self.username = username
    	self.password = password

    def __repr__(self):
        return '<username %r, password %r>' % (self.username, self.password)


if __name__ == '__main__':
    app.run()