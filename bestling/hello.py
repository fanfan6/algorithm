# coding=utf8

from flask import Flask, render_template, redirect, request, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo
from flask_login import login_user
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = 'fanfan'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


manager = Manager(app, db)
manager.add_command('db', MigrateCommand)
bootstrap = Bootstrap(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    passed = db.Column(db.String(40))

    def __repr__(self):
        return 'Role'.format(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))

    def __repr__(self):
        return 'Role'.format(self.username)


class NameForm(FlaskForm):
    name = StringField('username', validators=[DataRequired()])
    passwd = PasswordField('password', validators=[DataRequired(), EqualTo('passwd2')])
    passwd2 = PasswordField('password', validators=[DataRequired(), EqualTo('passwd')])
    remember_me = BooleanField("记住我")
    submit = SubmitField('submit')


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         user = form.name.filters()
#         name = form.name.data
#
#         form.name.data = ''
#     return render_template('index.html', form=form, name=name)

@app.route('/login', methods=['GET', 'POST'])
def wtf_login():
    form = NameForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.name.data
            passeord = form.passwd.data
    else:
        flash(u'请输入数据')

    return render_template('index.html', form=form)


@app.route('/user/<name>')
def user_name(name):
    return render_template('base.html', name=name)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    manager.run()
