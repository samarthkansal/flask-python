from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email

# this is comment added for github

class RegisterationForm(FlaskForm):
  username = StringField('UserName',validators=[DataRequired(),Length(min=2,max=20)])
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField('Sign Up')
  
class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Sign Up')

# This is a comment for branch and may be merged with master branch