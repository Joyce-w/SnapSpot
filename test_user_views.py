# import os

from unittest import TestCase
from models import db, connect_db, User, Post
# os.environ['DATABASE_URL'] = "postgresql:///shsi_test"

from app import app

db.drop_all()
db.create_all()

app.config['WTF_CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "secret_test")

class UserViewTestCase(TestCase):
    """test views for users"""

    def setUp(self):
        """Test what is displayed on homepage"""
        u1_test = User.signup(display_name='tester123',
                        username='tester123',
                        password="password",
                        area="Spain",
                        caption="")

        db.session.add(u1_test)
        db.session.commit()

        # setup login manager
        @app.login_manager.request_loader
        def load_user_from_request(request):
            return User.query.first()
        
        user = User.authenticate('tester1', 'password')
        
        self.u1_test = u1_test
        self.client = app.test_client()

    def test_homepage(self):
        """Test what is displayed on homepage"""

        with self.client as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            
            # user not logged in
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<li><a href="/login">Login</a></li>', html)
            self.assertIn('<li><a href="/explore">Explore</a></li>', html)
