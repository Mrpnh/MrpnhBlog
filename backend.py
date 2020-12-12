
"""
Packages needed for backend:
1) flask
2) jinja
3) flask-sqlalchemy
4) datetime
5) mysql-connector-python

"""



# imports
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy # orm(object relational mapping)
from datetime import datetime
import json

# Initialising things
with open("config.json","r") as f:
    params=json.load(f)["params"] 
local_server=True
app = Flask(__name__)
if local_server==True:
    app.config['SQLALCHEMY_DATABASE_URI']=params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI']=params["prod_uri"]
db = SQLAlchemy(app) # creating an instance of sqlalchemy

# To define database we need a class
class Contacts(db.Model):
    # You have to create below variable name same as the column name in database
    # This shows the structre of the table
    # And we create class so that we can pass arguments to fill them 
    slno= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    message = db.Column(db.String(300), nullable=False)
    contact_date = db.Column(db.String(12), nullable=True)

class Posts(db.Model):
    # You have to create below variable name same as the column name in database
    # This shows the structre of the table
    # And we create class so that we can pass arguments to fill them 
    Slno= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(100000), nullable=False)
    posted_by = db.Column(db.String(10), nullable=False)
    post_date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(20), nullable=True)



# endpoints

@app.route("/")
def home():
    return render_template('index.html',params=params)


@app.route("/about")
def about():
    return render_template('about.html',params=params)


@app.route("/contact",methods=['GET','POST'])
def contact():
    if (request.method=='POST') :
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        msg=request.form.get('msg')
        entry=Contacts(name=name,email=email,phone_number=phone,message=msg,contact_date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html',params=params)

@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html',params=params,post=post)



# app run
if __name__ == '__main__':
    app.run(port=5000,debug=True)
    