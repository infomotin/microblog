from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import EmailField

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Sign Up')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=20)])
    submit = SubmitField(label='Login')

class ReserPasswordForm(FlaskForm):           
    email = EmailField('Email', validators=[DataRequired(), Email()])           
    submit = SubmitField(label='Reset Password')

# token submit form
class ResetPasswordForm(FlaskForm):
    token = StringField('Token', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField(label='Reset Password')
