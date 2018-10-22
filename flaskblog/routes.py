from flask import render_template,url_for,flash,redirect
from flaskblog.forms import RegisterationForm,LoginForm    
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='Home', posts = info)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
      print("Inside IF::::::::::::")
      flash(f'The Account has been created for {form.username.data}!','success')
      return redirect(url_for('home'))
    else:
      print("Inside Else")
      print(form.errors)
    return render_template('register.html',title='Register',form = form)
	
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form = form)