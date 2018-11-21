from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email, ValidationError
from flaskblog.model import User,Post
from flask_login import current_user

# this is comment added for github

class RegisterationForm(FlaskForm):
  username = StringField('UserName',validators=[DataRequired(),Length(min=2,max=20)])
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField('Sign Up')
  
  def validate_user(self,username):
    userr = User.query.filter_by(username = username.data).first()
    if userr:
      raise ValidationError(f'This UserName is already taken, Please choose another username')
  
  def validate_email(self,email):
    email = User.query.filter_by(email = email.data).first()
    if email:
      raise ValidationError(f'This Email is already registered with us')
  
class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Password',validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Sign In')
  
class UpdateInformation(FlaskForm):
  username = StringField('UserName',validators=[DataRequired(),Length(min=2,max=20)])
  email = StringField('Email',validators=[DataRequired(),Email()])
  image = FileField('Update Profile Picture' , validators = [FileAllowed('png','jpg')])
  update = SubmitField('Update')
  
  def validate_username(self,username):
    if current_user.username != username.data:
      userr = User.query.filter_by(username = username.data).first()
      if userr:
        raise ValidationError(f'This UserName is already taken, Please choose another username')
  
  def validate_email(self,email):
    if current_user.email != email.data:
      emaill = User.query.filter_by(email = email.data).first()
      if emaill:
        raise ValidationError(f'This Email is already registered with us, Please User Different One')


# This is a comment for branch and may be merged with master branch