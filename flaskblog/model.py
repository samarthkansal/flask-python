from datetime import datetime
from flaskblog import db

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