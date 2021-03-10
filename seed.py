from models import User, Post, db
from app import app

db.drop_all()
db.create_all()

# Load users


u = User.signup(display_name='tester1',
                    username='tester1',
                    password="password",
                    area="",
                    caption="Hello there1")
                    
u1 = User.signup(display_name='tester2',
                    username='tester2',
                    password="password",
                    area="",
                    caption="what to say?")

u2 = User.signup(display_name='tester3',
                    username='tester3',
                    password="password",
                    area="hawaii",
                    caption="Hello3")

u3 = User.signup(display_name='tester4',
                    username='tester4',
                    password="password",
                    area="alaska",
                    caption="mahalo?!")

u4 = User.signup(display_name='tester5',
                    username='tester5',
                    password="password",
                    area="spain",
                    caption="")



db.session.add(u)
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)

db.session.commit()

# load posts

# Hawaii stuff
# https: // images.unsplash.com / photo - 1505852679233 - d9fd70aff56d?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80

# https://images.unsplash.com/photo-1545048984-76f238de07f6?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1269&q=80