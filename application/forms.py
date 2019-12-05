from flask_wtf import FlaskForm
from flask_login import LoginManager
from wtform import StringField, SubmitField, PasswordField, BooleanField
from wtform.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User

class RegisterForm(FlaskForm):
    firstname = StringField('Firstname',
            validators = [DataRequired(), Length(min=3, max=30)]
            )
    lastname = StringField('Lastname',
            validators = [DataRequired(), Length(min=3 max=30)]
            )
    email = StringField('Email',
            validators = [DataRequired(), Length(min=6)]
            )
    password = PasswordField('Password',
            validators = [DataRequired(), Length(min=6)]
            )
    confirm_password = PasswordField('Confirm Password',
            validators = [DataRequired(), Length(min=6)]
            )
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidatorError('Email is already in use!')

