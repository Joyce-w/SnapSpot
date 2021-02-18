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
        return f"<User id={u.id} name={u.name} species={u.species} hunger = {u.hunger}>"

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




