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

class UserViewsTestCase(TestCase):
    """Test views for users"""

    def setUp(self):
        """Add sample user"""

        User.query.delete()
        Post.query.delete()

        user = User.signup(display_name='Tester1',
                            username='TestUser1',
                            password="password",
                            caption="tester 1 has entered")

        db.session.add(user)
        db.session.commit()

        self.user = user
        self.user.username = user.username
        # create test post for user
        p1 = Post(title="test title", image="https://images.unsplash.com/photo-1509840841025-9088ba78a826?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", description="This is a test2", lat=38.9196, lng=-2.0507, created_dt="2021-03-16 10:45:53.875247", place_name="Testopia", user_id=self.user.id)

        db.session.add(p1)
        db.session.commit()
        self.p1 = p1
        self.p1_id = p1.id

        self.client = app.test_client()

    def tearDown(self):
        """Clean up session"""
        db.session.rollback()

    def test_homeroute(self):
        """test model on homepage"""

        with self.client as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<a class="uk-text-bold">Get Started </a>', html)
            self.assertIn('<li><a href="/explore">Explore</a></li>', html)

    def test_posts(self):
        """test user views on post"""

        with self.client as client:
            resp = client.get(f"/post/{self.p1_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('Edit</a>', html)
            
    def test_user_pg(self):
        """test user views"""

        with self.client as client:
            resp = client.get(f"/users/{self.user.username}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn('<div class="user_btns">', html)
            self.assertNotIn('<a href="/logout">', html)

    def test_users(self):
        """Test list of users"""

        with self.client as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<a href="/users/{self.user.username}">', html)

