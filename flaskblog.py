from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

from forms import RegisterationForm,LoginForm

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
app.config['SECRET_KEY'] = '5af72aa71c28803e25316082282d760a'
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(20),unique = True, nullable = False)
  email = db.Column(db.String(120),unique = True, nullable = False)
  password = db.Column(db.String(20), unique=False,nullable = False)
  image_file = db.Column(db.String(20),default='default.jpg', nullable = False)
  posts = db.relationship('Post',backref ='post',lazy = True)
  
  def __repr__(self):
    return f"User('{self.username}','{self.email}','{self.image_file}')"
  
class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(120),nullable = False)
  dateposted = db.Column(db.DateTime, nullable = False , default = datetime.utcnow)
  content = db.Column(db.Text,nullable = False)
  user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable = False)
  
  def __repr__(self):
    return f"Post('{self.title}','{self.dateposted}','{self.content}')"
    
    
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
	
if __name__ == '__main__':
  app.run(debug = True)