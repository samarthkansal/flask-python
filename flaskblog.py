from flask import Flask,render_template,url_for,flash,redirect
app = Flask(__name__)

from forms import RegisterationForm,LoginForm

info = [
       {"Name": "Samarth",
	    "Age" : "27",
		"Status" :"UM",
		"Company" : "UTC"
	   },
	   
	   {"Name": "Sam",
	    "Age" : "26",
		"Status" :"UM",
		"Company" : "Rockwell Collins"
	   }
]
app.config['SECRET_KEY'] = '5af72aa71c28803e25316082282d760a'

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