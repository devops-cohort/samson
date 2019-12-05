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

    # Checking the email to make sure it's not already in the database
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidatorError('Email is already in use!')

    # Checking the password to make sure it has uppercase, lowercase, an integer and is at least 6 characters long    
    def validate_password(self, password):
        valid = True
        if len(password.data < 6):
            valid = False
            ValidatorError('Password needs to be more than 6 characters')
        elif not re.search([A-Z], password.data):
            valid = False
            ValidatorError('Password needs to have UPPERCASE characters')
        elif not re.search([a-z], password.data):
            valid = False
            ValidatorError('Password needs to have LOWERCASE characters')
        elif not re.search([0-9], password.data):
            valid = False
            ValidatorError('Password needs to have NUMBERS')
        # If the validation conditions are not met then show the following error message 
        if valid == False:
            ValidatorError('Password needs to have UPPERCASE, LOWERCASE, NUMBERS and must be at least 6 characters long')

    # Checking if the confirm password field matches the password field
    def validate_confirm_password(self, confirm_password):
        if confirm_password.data != password.data:
            raise ValidatorError('Passwords do not match!')
