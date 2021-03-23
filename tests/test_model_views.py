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


class PostViewsTestCase(TestCase):
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

        self.u1_id = u1.id
        self.u1_username = u1.username
        self.u2_id = u2.id
        self.u3_id = u3.id

        # create test post for test user
        p1 = Post(title="test title", image="https://images.unsplash.com/photo-1509840841025-9088ba78a826?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", description="This is a test1", lat=38.9196, lng=-2.0507, created_dt="2021-03-16 10:45:53.875247", place_name="Testopia", user_id=self.u1_id)

        p2 = Post(title="test title2", image="https://images.unsplash.com/photo-1509840841025-9088ba78a826", description="This is a test2", lat=38.9196, lng=-2.0507, created_dt="2021-03-15 10:45:53.875247", place_name="Testopia", user_id=self.u2_id)
        
        p3 = Post(title="test title3", image="https://images.unsplash.com/photo-1509840841025-9088ba78a826", description="This is a test3", lat=38.9196, lng=-2.0507, created_dt="2021-03-16 10:45:53.875247", place_name="Testopia", user_id=self.u1_id)
       
        p4 = Post(title="test title4", image="https://images.unsplash.com/photo-1509840841025-9088ba78a826", description="This is a test4", lat=38.9196, lng=-2.0507, created_dt="2008-03-16 10:45:53.875247", place_name="Testopia", user_id=self.u2_id)
        
        p5 = Post(title="test title5", image="https://images.unsplash.com/photo-1509840841025-9088ba78a826", description="This is a test5", lat=38.9196, lng=-2.0507, created_dt="2020-03-16 10:45:53.875247", place_name="Testopia", user_id=self.u3_id)

        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.add(p4)
        db.session.add(p5)
        db.session.commit()

        self.p1_id = p1.id
        self.p2_id = p2.id
        self.p3_id = p3.id
        self.p4_id = p4.id
        self.p5_id = p5.id
        
        self.p1_title = p1.title
        self.p1_user = p1.user_id

        f1 = Favorite(post_id=self.p1_id, user_id=self.u1_id)
        f2 = Favorite(post_id=self.p1_id, user_id=self.u2_id)
        f3 = Favorite(post_id=self.p1_id, user_id=self.u3_id)

        f4 = Favorite(post_id=self.p2_id, user_id=self.u1_id)
        f6 = Favorite(post_id=self.p2_id, user_id=self.u3_id)

        f8 = Favorite(post_id=self.p3_id, user_id=self.u2_id)
        f9 = Favorite(post_id=self.p3_id, user_id=self.u3_id)

        db.session.add(f1)
        db.session.add(f2)
        db.session.add(f3)
        db.session.add(f4)
        db.session.add(f6)
        db.session.add(f8)
        db.session.add(f9)
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        """Clean transactions"""
        db.session.rollback()

    def test_home_pg(self):
        """Test if trending/recent posts are displayed"""

        with self.client as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # p1 should be top 3 in trending while p4 is not
            self.assertIn(f'<a href="/post/{self.p1_id}">', html)
            self.assertNotIn(f'<a href="/post/{self.p4_id}">', html)
            # p5 is oldest post and should not appear
            self.assertNotIn(f'<a href="/post/{self.p5_id}">', html)


    def test_user_posts(self):
        """Test post that users published"""
        with self.client as client:
            resp = client.get(f"/users/{self.u1_username}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            # u1 owns p1 but not p2
            self.assertIn(f'<a class="uk-button uk-button-text" href="/post/{self.p1_id}">', html)
            self.assertNotIn(f'<a class="uk-button uk-button-text" href="/post/{self.p2_id}">', html)