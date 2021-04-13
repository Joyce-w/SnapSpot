from flask import Flask, request, render_template,  redirect, flash, session, json, g
import requests, pdb
from collections import Counter
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post, Favorite
from forms import UserSignup, UserLogin, NewPost
from sqlalchemy.exc import IntegrityError
import os

MAPBOX_TOKEN = "pk.eyJ1Ijoiam95am95am95eSIsImEiOiJja2w4YzZyM3kxcTdmMnZwZXdiNG5yczRjIn0.CDJtfCb3X8TKcTBRMPBJFA"

CURR_USER = "curr_user"

# app created 
app = Flask(__name__)


# specify that youre using postgres and a specific database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///shsi_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'w12z8wwdxcfa')
print(app.config['SECRET_KEY'])
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

    # Display random pics for silder 
    post = Post.query.limit(3).all()

    # Display recent posts from db
    recent_posts = Post.query.order_by(Post.created_dt.desc()).limit(3).all()

    # display trending posts
    test = Favorite.query.all()

    # returns all post_id for obj from query
    arr = [p.post_id for p in test]
    
    # returns post_id of the most likes 
    ids = [p[0] for p in Counter(arr).most_common(3)]
    
    # post_ids are returned numerically asc, order by popularity
    top_posts = Post.query.filter(Post.id.in_(ids)).all()
    
    # Use favorites to count top 
    return render_template('homepage.html',post=post, recent=recent_posts, top=top_posts)

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
        try:
            # signup user with User classmethod
            user = User.signup(display_name=form.display_name.data,
                                username=form.username.data,
                                password=form.password.data,
                                caption=form.caption.data)

            db.session.commit()
            flash("Account created! Please sign-in to get started.", 'success')
            return redirect("/login")

        except IntegrityError:
            flash("Username is already taken, try something else!", 'danger')
    return render_template('/users/signup.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    """Display login form"""
    
    form = UserLogin()

    if g.user:
        flash("You have been automatically logged-out. Please try logging in again.", "success")
        return redirect("/logout")
        
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

    post = Post.query.all()

    # dict to parse on tempalte and display corresponding info
    points = [{'id': p.id, 'coords':[p.lng, p.lat], "img": p.image} for p in post]

    return render_template('map.html',token=token , points=points)

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
        time =  datetime.now()

        #return coordinates [lng, lat] format for db storage 
        lat = float(request.form['coord_lat'])
        lng = float(request.form['coord_lng'])

        # get location name
        location_url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{lng},{lat}.json?access_token={MAPBOX_TOKEN}"

        res = requests.get(location_url).json()
        loc = res['features'][0]['place_name']


        user=g.user.id

        new_post = Post(title=title, image=image, description=description, lat=lat, lng=lng, created_dt=time, place_name=loc, user_id=user)
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

    post_favs = msg = Favorite.query.filter(Favorite.post_id==post_id).all()
    user_faved = [f.user_id for f in post_favs]

    return render_template('/posts/post_detail.html', post=post,user_faved=user_faved)


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
    
    # Keep old info if form input is left blank on submission
    if new_title == '':
        new_title = post.title
        
    if new_desc == '':
        new_desc = post.description
        
    # update info in db
    post.title = new_title 
    post.description = new_desc
    db.session.commit()

    flash("Post successfully updated!", 'success')
    # redirect back to post owner
    post_owner = post.users
    username = post_owner.username    

    return redirect(f"/users/{username}")


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


# ---------Liking/unliking a post -----------

@app.route("/post/<int:post_id>/favorite", methods=["GET", "POST"])
def fav_post(post_id):
    """Handle likes for a post"""

    if g.user:
        user = g.user.id

        post_favs = msg = Favorite.query.filter(Favorite.post_id==post_id).all()
        user_faved = [f.user_id for f in post_favs]

        # check if user id is in the users that favorited the post
        if user in user_faved:
            msg = Favorite.query.filter(Favorite.post_id==post_id, Favorite.user_id==user).delete()
            db.session.commit()
        # if user has not favorited 
        else:
            f = Favorite(post_id=post_id, user_id=user)
            db.session.add(f)
            db.session.commit()

        return redirect(f"/post/{post_id}")
    # Throw warning if there is no user
    else:
        flash("Please login or create an account to favorite this post!", "danger")
        return redirect(f"/post/{post_id}")