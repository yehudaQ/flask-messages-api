from wtforms import Form, StringField, PasswordField, validators


class RegistrationForm(Form):
    email = StringField('email', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.Length(min=6, max=35),
        validators.EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField('confirm_password', [validators.DataRequired()])


class MessageForm(Form):
    receiver_email = StringField('receiver_email', [validators.Email()])
    message = StringField('message', [validators.DataRequired(), validators.Length(min=1, max=250)])
    subject = StringField('subject', [validators.DataRequired(), validators.Length(min=1, max=150)])
