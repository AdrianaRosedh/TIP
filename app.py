from flask import Flask, render_template, redirect
from flask.helpers import url_for
from flask_bootstrap import Bootstrap
from flask_login.utils import logout_user
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user
from flask_login.mixins import UserMixin

from wtforms import StringField, PasswordField
from wtforms.validators import Length, Email

from werkzeug.security import generate_password_hash, check_password_hash

from dash_application import create_kpi1, create_kpi2, create_kpi3, create_kpi4, create_kpi5, create_kpi6

app = Flask(__name__)
app.config["SECRET_KEY"] = "THIS IS A SECRET, DON'T DO THIS!"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.db"
Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager()
login.init_app(app)
create_kpi1(app)
create_kpi2(app)
create_kpi3(app)
create_kpi4(app)
create_kpi5(app)
create_kpi6(app)



@login.user_loader
def user_loader(user_id):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)


class LoginForm(FlaskForm):
    email = StringField("email", validators=[Email()])
    password = PasswordField("password", validators=[Length(min=5)])


class RegisterForm(FlaskForm):
    email = StringField("email", validators=[Email()])
    password = PasswordField("password", validators=[Length(min=5)])
    repeat_password = PasswordField("repated_password", validators=[Length(min=5)])


@app.route("/")
def index():
    return render_template("dashboards.html")

@app.route("/raised")
def kpi1():
    return render_template("KPI1.html")

@app.route("/solved")
def kpi2():
    return render_template("KPI2.html")

@app.route("/sla")
def kpi3():
    return render_template("KPI3.html")

@app.route("/backlog")
def kpi4():
    return render_template("KPI4.html")

@app.route("/service")
def kpi5():
    return render_template("KPI5.html")

@app.route("/availability")
def kpi6():
    return render_template("KPI6.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if check_password_hash(user.password, form.password.data):
            login_user(user)

            return redirect(url_for("index"))

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit() and form.password.data == form.repeat_password.data:
        user = User(
            email=form.email.data, password=generate_password_hash(form.password.data)
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("register.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug = True)