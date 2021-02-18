from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post
from forms.new_post_form import NewPost


# app created 
app = Flask(__name__)

# specify that youre using postgres and a specific database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///shsi_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "wheredoyouwanttogo0217"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

#call connect_db from models
connect_db(app)
    
@app.route('/')
def homepage():
    """Show homepage"""

    return render_template('homepage.html')

@app.route('/new-post')
def new_post():
    """Load form to share a location"""

    form = NewPost()

    return render_template('new_post.html', form=form)