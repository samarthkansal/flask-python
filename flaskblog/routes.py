from flask import render_template,url_for,flash,redirect
from flaskblog.forms import RegisterationForm,LoginForm   
from flaskblog import app,db
from flaskblog.model import User
from flaskblog import bcrypt
from flaskblog import login_manager 
from flask_login import login_user,logout_user

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

info = [{
         "Name": "Samarth Kansal",
         "Age" : "27",
		 "Organisation": "RC India",
		 "Status": "UP"

        },
		{
		 "Name": "Sammy Kansal",
         "Age" : "27",
		 "Organisation": "RC India",
		 "Status": "UP"
		}]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='Home', posts = info)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
      hashed_password =  bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username = form.username.data, email = form.email.data, password = hashed_password)
      db.session.add(user)
      db.session.commit()
      flash(f'The Account has been created for {form.username.data}!','success')
      return redirect(url_for('home'))
    else:
      return render_template('register.html',title='Register',form = form)
	
@app.route("/login", methods = [ 'GET', 'Post'])
def login():
    form = LoginForm()
    user = User.query.filter_by(email = form.email.data).first()
    if user and bcrypt.check_password_hash(user.password,form.password.data)
      redirect(url_for('home'))
      logout_user(user,remember)
    return render_template('login.html',title='Login',form = form)