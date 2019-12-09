from flask_wtf import FlaskForm
from flask_login import LoginManager
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User, Anime, Anime_Watching, Anime_Completed
import re

class RegisterForm(FlaskForm):
    firstname = StringField('Firstname',
            validators = [DataRequired(), Length(min=3, max=30)]
            )
    lastname = StringField('Lastname',
            validators = [DataRequired(), Length(min=3, max=30)]
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
            raise ValidationError('Email is already in use!')

    # Checking the password to make sure it has uppercase, lowercase, an integer and is at least 6 characters long    
    def validate_password(self, password):
        valid = True
        if len(password.data) < 6:
            valid = False
            ValidationError('Password needs to be more than 6 characters')
        elif not re.search(r'[A-Z]', password.data):
            valid = False
            ValidationError('Password needs to have UPPERCASE characters')
        elif not re.search(r'[a-z]', password.data):
            valid = False
            ValidationError('Password needs to have LOWERCASE characters')
        elif not re.search(r'[0-9]', password.data):
            valid = False
            ValidationError('Password needs to have NUMBERS')
        # If the validation conditions are not met then show the following error message 
        if valid == False:
            ValidationError('Password needs to have UPPERCASE, LOWERCASE, NUMBERS and must be at least 6 characters long')

    # Checking if the confirm password field matches the password field
    def validate_confirm_password(self, confirm_password):
        if confirm_password.data != self.password.data:
            raise ValidationError('Passwords do not match!')

class LoginForm(FlaskForm):
    email = StringField('Email',
            validators = [DataRequired(), Email()]
            )
    password = PasswordField('Password', 
            validators = [DataRequired()]
            )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class AddWatching(FlaskForm):
    watch = SubmitField('Watching')

class UpdatePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password',
            validators = [DataRequired(), Length(min=6)]
            )
    new_password = PasswordField('New Password',
            validators = [DataRequired(), Length(min=6)]
            )
    confirm_password = PasswordField('Confirm Password',
            validators = [DataRequired(), Length(min=6)]
            )
    submit = SubmitField('Update')

    def check_Old_Password(self, old_password):
        if current_user.password != old_password.data:
            user = User.query.filter_by(password=old_password.data).first()
            raise ValidationError('Wrong password')



    def validate_password(self, new_password):
        valid = True
        if len(new_password.data) < 6:
            valid = False
            ValidationError('Password needs to be more than 6 characters')
        elif not re.search(r'[A-Z]', new_password.data):
            valid = False
            ValidationError('Password needs to have UPPERCASE characters')
        elif not re.search(r'[a-z]', new_password.data):
            valid = False
            ValidationError('Password needs to have LOWERCASE characters')
        elif not re.search(r'[0-9]', new_password.data):
            valid = False
            ValidationError('Password needs to have NUMBERS')
        # If the validation conditions are not met then show the following error message
        if valid == False:
            ValidationError('Password needs to have UPPERCASE, LOWERCASE, NUMBERS and must be at least 6 characters long')

    # Checking if the confirm password field matches the password field
    def validate_confirm_password(self, confirm_password):
        if confirm_password.data != self.new_password.data:
            raise ValidationError('Passwords do not match!')

