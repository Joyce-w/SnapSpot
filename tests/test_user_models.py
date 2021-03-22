import os

from unittest import TestCase
from models import db, connect_db, User, Post, Favorite
os.environ['DATABASE_URL'] = "postgresql:///shsi_test"

from app import app

app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "secret_test")

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """Test models for users"""

    def setUp(self):
        """Add sample user"""
        User.query.delete()

    def tearDown(self):
        """Clean transactions"""
        db.session.rollback()

    def test_user(self):
        """Retrieve user information"""

        # create test user
        u1 = User.signup(display_name='Test User 1',
                username='tester1',
                password="password",
                caption="i am test user 1")

        db.session.add(u1)
        db.session.commit()
        self.u1 = u1
        user = User.query.get(u1.id)

        self.assertEqual(user.display_name, 'Test User 1')
        self.assertEqual(user.caption, "i am test user 1")

    def test_user_post(self):
        """Retrieve user post info"""

        # create test user
        u1 = User.signup(display_name='Test User 1',
                username='tester1',
                password="password",
                caption="i am test user 1")

        db.session.add(u1)
        db.session.commit()
        self.u1 = u1
        user = User.query.get(u1.id)

        # create test post for user
        p1 = Post(title="test title", image="https://images.unsplash.com/photo-1509840841025-9088ba78a826?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", description="This is a test", lat=38.9196, lng=-2.0507, created_dt="2021-03-16 10:45:53.875247", place_name="Spain", user_id=u1.id)

        db.session.add(p1)
        db.session.commit()
        self.p1 = p1

        # create user fav
        f1 = Favorite(post_id=p1.id, user_id=u1.id)

        db.session.add(f1)
        db.session.commit()
        self.f1 = f1

        user = User.query.get(u1.id)
        u_posts = user.posts
        fav = Favorite.query.all()

        self.assertEqual(len(u_posts), 1)
        self.assertEqual(len(fav), 1)
        self.assertEqual(p1.users.username, "tester1")
        self.assertEqual(user.display_name, 'Test User 1')
        self.assertEqual(user.caption, "i am test user 1")


