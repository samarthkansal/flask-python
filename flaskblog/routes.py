from flask import render_template,url_for,flash,redirect
from flaskblog.forms import RegisterationForm,LoginForm   
from flaskblog import app,db
from flaskblog.model import User
from flaskblog import db
from flaskblog import bcrypt

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
    print ("Errors:::::::::::",form.errors)
    if form.validate_on_submit():
      hashed_password =  bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username = form.username.data, email = form.email.data, password = hashed_password)
      db.session.add(user)
      db.session.commit()
      flash(f'The Account has been created for {form.username.data}!','success')
      return redirect(url_for('home'))
    else:
      return render_template('register.html',title='Register',form = form)
	
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form = form)