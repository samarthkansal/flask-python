from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
print("apppp#########: ",app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
app.config['SECRET_KEY'] = '5af72aa71c28803e25316082282d760a'
db = SQLAlchemy(app)

from flaskblog import routes