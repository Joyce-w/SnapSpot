from flask import Flask, request, render_template,  redirect, flash, session, json, g
import requests
import pdb
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post
from forms import UserSignup, UserLogin, NewPost
from secrets import MAPBOX_TOKEN


CURR_USER = "curr_user"

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
login_manager = LoginManager()
login_manager.init_app(app)

@app.before_request
def g_user():
    """Set token"""

    session['token'] = MAPBOX_TOKEN
    
    if '_user_id' in session:
        g.user = User.query.get(session['_user_id'])

    else:
        g.user = None
    

@app.route('/')
def homepage():
    """Show homepage"""

    post = Post.query.limit(4).all()

    return render_template('homepage.html',post=post)

# flask-login stuff
# get user object
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#----------------- login and signup ----------------#

@app.route('/register', methods=["GET", "POST"])
def signup():
    """Display signup page"""

    form = UserSignup()

    if form.validate_on_submit():
        # signup user with User classmethod
        user = User.signup(display_name=form.display_name.data,
                            username=form.username.data,
                            password=form.password.data,
                            area=form.area.data,
                            caption=form.caption.data)

        db.session.commit()
        flash("Account created! Please sign-in to get started.", 'success')
        return redirect("/login")

    return render_template('/users/signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    """Display login form"""
    
    form = UserLogin()

    if form.validate_on_submit():
        # signup user with User classmethod
        username = form.username.data
        pwd = form.password.data

        # authenticate the user
        user = User.authenticate(username, pwd)
        
        if user:
            login_user(user)
            return redirect("/")
        else:
            flash("Username or password is incorrect!",'danger')



    return render_template('/users/login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    """logout current user"""
    logout_user()
    return redirect('/')



@app.route('/explore')
def explore():
    """Load map with pinned locations"""

    token = MAPBOX_TOKEN
    
    point = [
            [-118.1661, 33.9446],
            [-118.0, 32.9446],
            [-51.1661, -71.0],
            [21.1661, -61.0],
            [102.35651371624147, 36.88396914522427]
    ]

    return render_template('map.html',token=token , point=point)

@app.route('/location-picker')
@login_required
def find_location():
    """Find coordinates for post"""

    return render_template('find_coord.html')

# ------------  Post routes  -----------
@app.route('/new-post', methods=["GET", "POST"])
@login_required
def new_post():
    """Find coordinates for post"""

    form = NewPost()

    if form.validate_on_submit():
        # make new model
        
        title = form.title.data
        image = form.image.data
        description = form.description.data

        #return coordinates [lng, lat] format for db storage 
        lat = float(request.form['coord_lat'])
        lng = float(request.form['coord_lng'])
        location = [lng, lat]

        
        user=g.user.id

        new_post = Post(title=title, image=image, description=description, location=location, user_id=user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(f"/users/{g.user.username}") 
    else:
        return render_template('/posts/new_post.html', form=form)

    return render_template('/posts/new_post.html', form=form)


@app.route('/post/<int:post_id>')
def view_post(post_id):
    """View a single post's details"""

    post = Post.query.get(post_id)

    return render_template('/posts/post_detail.html', post=post)


@app.route('/post/<int:post_id>/edit', methods=["GET"])
@login_required
def get_post(post_id):
    """Allow owners to edit their post"""

    post = Post.query.get(post_id)

    return render_template('/posts/edit_form.html', post=post)


@app.route('/post/<int:post_id>/edit', methods=["POST"])
@login_required
def edit_post(post_id):
    """Allow owners to edit their post"""

    post = Post.query.get(post_id)

    new_title = request.form['new_title'] 
    new_desc = request.form['new_desc']

    # update infor in db
    post.title = new_title
    post.description = new_desc
    db.session.commit()

    return redirect("/users")


@app.route('/post/<int:post_id>/delete')
@login_required
def del_post(post_id):
    """Allow owners to delete their own post"""

    post = Post.query.filter_by(id=post_id).delete()
    db.session.commit()

    # Flash message about deletion
    flash("Post deleted.")
    
    return redirect("/users")

# --------User Routes -----------#

@app.route('/users')
def display_users():
    """Display all users"""
    
    users = User.query.all()
    return render_template('/users/all_users.html', users=users)


@app.route('/users/<username>')
def user_info(username):
    """Display single user"""
    
    user = User.query.filter_by(username=username).first()
    return render_template('/users/user.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    """Display form to edit user"""
    user = User.query.get(user_id)

    if user.id == session['_user_id']:
        # display user edit form
        form = UserSignup(obj=user)

        if form.validate_on_submit():
            user.username = form.username.data
            user.display_name = form.display_name.data
            user.area = form.area.data
            user.caption = form.caption.data
            db.session.commit()
            flash('User information updated!', 'success')
            return redirect(f"/users/{user.username}")

        return render_template('/users/edit_user.html', user=user, form=form)

    else:
        flash("You do not have permission to make changes to this user!")

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=["POST"])
@login_required
def delete_user(user_id):
    """Delete user"""
    user = User.query.get(user_id)

    if user.id == session['_user_id']:    
        db.session.delete(user)
        db.session.commit()
        logout_user()
        return redirect("/register")

    else:
        flash('You do not have permission to delete this account', 'danger')
        return redirect('/users')
