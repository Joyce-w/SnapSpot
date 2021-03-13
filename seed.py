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


p1 = Post(title='Guadalajara', image='https://images.unsplash.com/photo-1601109471554-7429b4103cba?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80', description='description', lat=20.7065585989509, lng=-103.36582497984853, user_id=2)

p2 = Post(title='Svalbard', image='https://images.unsplash.com/photo-1569097269234-dd5253cf3294?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80', description='description', lat=78.79872466392445, lng= 17.29448838441985, user_id=3)

p3 = Post(title='Brazill', image='https://images.unsplash.com/photo-1483729558449-99ef09a8c325?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80', description='description', lat=-8.51713144204551 ,lng= -42.16729206114363, user_id=2)


db.session.add(p1)
db.session.add(p2)
db.session.add(p3)

db.session.commit()