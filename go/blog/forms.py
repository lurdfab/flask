from blog import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField,TextAreaField
from wtforms.validators import InputRequired, email_validator, Length, ValidationError, email, DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), email(message='invalid email'), Length(max=30)])
    password=PasswordField('Password', validators=[InputRequired(), Length(min=10, max=15)])

class SignUpForm(FlaskForm):
    first_name=StringField('First Name', validators=[InputRequired(), Length(min=3, max=30)])
    last_name=StringField('Last Name', validators=[InputRequired(), Length(min=3, max=30)])
    email=StringField('Email', validators=[InputRequired(), email(message='invalid email'), Length(min=20, max=30)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=10, max=15)])

class ContactUsForm(FlaskForm):
    first_name=StringField('First Name', validators=[InputRequired(), Length(min=3, max=30)])
    last_name=StringField('Last Name', validators=[InputRequired(), Length(min=3, max=30)])
    email=StringField('Email', validators=[InputRequired(), email(message='invalid email'), Length(min=20, max=30)])
    comments=TextAreaField('Comments', validators=[InputRequired(), Length(min=100, max=1000)])