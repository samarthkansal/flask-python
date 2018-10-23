from flask import render_template,url_for,flash,redirect
from flaskblog.forms import RegisterationForm,LoginForm   
from flaskblog import app 

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
      flash(f'The Account has been created for {form.username.data}!','success')
      return redirect(url_for('home'))
    else:
     return render_template('register.html',title='Register',form = form)
	
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form = form)