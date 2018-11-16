from flask import render_template,url_for,flash,redirect,request
from flaskblog.forms import RegisterationForm,LoginForm, UpdateInformation  
from flaskblog import app,db,bcrypt
from flaskblog.model import User
from flask_login import login_user,logout_user,current_user,login_required


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
      return redirect(url_for('login'))
    else:
      return render_template('register.html',title='Register',form = form)
	
@app.route("/login", methods = [ 'GET', 'Post'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email = form.email.data).first()
    if user and bcrypt.check_password_hash(user.password,form.password.data):
      login_user(user,remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(url_for('home')) if not next_page else redirect(next_page)
    else: 
      flash(f"Login Unsuccessful! Invalid Email Id or Password", 'danger')
  return render_template('login.html',title='Login', form = form)
    
@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('login'))
  
@app.route("/account")
@login_required
def account():
  form = UpdateInformation()
  image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
  return render_template('account.html', title ='Account' ,image_file = image_file, form = form)

  