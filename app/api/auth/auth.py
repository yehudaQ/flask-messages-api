from flask import Blueprint, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.core.forms import RegistrationForm, LoginForm
from app.models.user import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    # TODO : Handle response Status Codes
    # TODO : Request data format
    if request.method == 'POST':
        form = LoginForm(ImmutableMultiDict(request.get_json()))
        if not form.validate():
            return form.errors, 403

        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                return "Logged in!", 200

            return 'Password is incorrect!', 401

        return 'Email does not exist!', 401

    # Get method
    return str(current_user), 200


@auth.route("/sign-up", methods=['POST'])
def sign_up():
    form = RegistrationForm(ImmutableMultiDict(request.get_json()))
    if not form.validate():
        return form.errors, 403

    email_exists = User.query.filter_by(email=form.email.data).first()

    if email_exists:
        return 'Email is already in use.', 403

    new_user = User(email=form.email.data, password=generate_password_hash(form.password.data, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user, remember=True)

    return 'User successfully created.', 201


@auth.route("/logout", methods=['POST'])
@login_required
def logout():
    logout_user()
    return 'The user successfully logged out.', 200
