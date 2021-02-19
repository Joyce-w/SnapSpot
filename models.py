from flask_sqlalchemy import SQLAlchemy

# initalize SQLA 
db = SQLAlchemy()

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
        return f"<User id={u.id}, name={u.name}, username={u.username}>"

    #define individual col in user table
    id = db.Column(db.Integer,
                    primary_key = True,
                    autoincrement=True)

    name = db.Column(db.String(30),
                    nullable=False)
    
    username = db.Column(db.String(30),
                    nullable=False,
                    unique=True)
    
    password = db.Column(db.String(30),
                    nullable=False)
    
    # references
    posts = db.relationship('Post', backref='users')


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

    location = db.Column(db.String(30),
                    nullable=False)
    
    image = db.Column(db.String())
    
    description = db.Column(db.String(200))

    user_id = db.Column(db.Integer,
                db.ForeignKey('users.id'))