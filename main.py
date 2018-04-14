from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://
build-a-blog:buildtheblog@localhost:8889/get-it-done'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

Class Blog(db.Model)

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(120))
        body = db.Column(db.String(900))





@app.route('/', methods=['Post', 'GET'])
def index():






@app.route('blog', methods=['POST'])
def Blog():




@app.route('newpost', methods=['POST'])
def newpost():