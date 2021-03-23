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



class PostModelTestCase(TestCase):
    """Test models for users"""

    def setUp(self):
        """Add sample user"""
        Post.query.delete()

        # create test user
        user = User.signup(display_name='Test User 1',
                username='tester1',
                password="password",
                caption="i am test user 1")

        db.session.add(user)
        db.session.commit()
        self.user = user
        self.user_id = user.id

        # create test post for test user
        p1 = Post(title="test title", image="https://images.unsplash.com/photo-1509840841025-9088ba78a826?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", description="This is a test2", lat=38.9196, lng=-2.0507, created_dt="2021-03-16 10:45:53.875247", place_name="Testopia", user_id=self.user.id)

        db.session.add(p1)
        db.session.commit()
        self.p1 = p1
        self.p1_title = p1.title
        self.p1_user = p1.user_id

    def tearDown(self):
        """Clean transactions"""
        db.session.rollback()

    def test_post(self):
        """Retrieve user information"""

        self.assertEqual(self.p1_title, 'test title')
        self.assertEqual(self.p1_user, self.user_id)



class FavModelTestCase(TestCase):
    """Test models for users"""

    def setUp(self):
        """Add sample user/post/fav"""
        User.query.delete()
        Post.query.delete()
        Favorite.query.delete()

        # create test user
        u1 = User.signup(display_name='test1',
                username='Tester1',
                password="password",
                caption="i am test user 1")

        u2 = User.signup(display_name='test2',
                            username='Tester2',
                            password="password",
                            caption="test2")

        u3 = User.signup(display_name='test3',
                            username='Tester3',
                            password="password",
                            caption="im tester 3")

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)
        db.session.commit()

        self.u1 = u1
        self.u1_id = u1.id
        self.u2_id = u2.id
        self.u3_id = u3.id

        # create test post for test user
        p1 = Post(title="test title", image="https://images.unsplash.com/photo-1509840841025-9088ba78a826?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", description="This is a test2", lat=38.9196, lng=-2.0507, created_dt="2021-03-16 10:45:53.875247", place_name="Testopia", user_id=self.u1.id)

        db.session.add(p1)
        db.session.commit()
        self.p1_id = p1.id
        self.p1_title = p1.title
        self.p1_user = p1.user_id

        f1 = Favorite(post_id=self.p1_id, user_id=self.u1_id)
        f2 = Favorite(post_id=self.p1_id, user_id=self.u2_id)
        f3 = Favorite(post_id=self.p1_id, user_id=self.u3_id)

        db.session.add(f1)
        db.session.add(f2)
        db.session.add(f3)
        db.session.commit()

    def tearDown(self):
        """Clean transactions"""
        db.session.rollback()

    def test_Fav(self):
        """Test Favorite model"""

        fav = Favorite.query.all()
        self.assertEqual(len(fav), 3)
