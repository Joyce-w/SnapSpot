from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# initalize SQLA 
db = SQLAlchemy()
bcrypt = Bcrypt()

#connect app with SQLA instance
#call logic to connect to db from app.py, don't want to happen everytime models.py is ran
def connect_db(app):
    db.app = app
    db.init_app(app)

# MODELS GO BELOW
class User(db.Model):
    #special dunder method to determine table name
    __tablename__ = "users"

    def __repr__(self):
        u=self
        return f"<User id={u.id}, display_name={u.display_name}, username={u.username}>"

    #define individual col in user table
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement=True)

    display_name = db.Column(db.String(30),
                    nullable=False)
    
    username = db.Column(db.String(30),
                    nullable=False,
                    unique=True)
    
    password = db.Column(db.String(),
                    nullable=False)

    area = db.Column(db.String(),
                    nullable=False)
    
    # references
    posts = db.relationship('Post', backref='users')


    @classmethod
    def signup(cls, display_name, username, password, area):
        """Signup user and hash password"""
        
        hashed_pw = bcrypt.generate_password_hash(password).decode("utf8")

        user = User(display_name=display_name,
                    username=username,
                    password=hashed_pw,
                    area=area)

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Authenticate user when logging in"""

        pwd = bcrypt.generate_password_hash(password)
        user = User.query.filter_by(username=username, password=password).first()
        
        if bcrypt.check_password_hash(pwd, password):
            return user

        

class Post(db.Model):

    __tablename__ = "posts"

    def __repr__(self):
        p=self
        return f"<Post id={p.id}, location={p.location}, image={p.image}, description={p.description}, user_id={p.user_id}>"
   
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement=True)
                    
    title = db.Column(db.String(),
                    nullable=False)

    location = db.Column(db.String(),
                    nullable=False)
    
    image = db.Column(db.String())
    
    description = db.Column(db.String(200))

    user_id = db.Column(db.Integer,
                db.ForeignKey('users.id'))

                