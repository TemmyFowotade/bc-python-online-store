"""Testing for the application
"""

import unittest
from flask.ext.testing import TestCase
from app import app, db
from app.models import User, Store
from config import config


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object(config['testing'])
        return app

    def setUp(self):
        db.create_all()

    def test_01_that_user_can_sign_up(self):
        response = self.client.get('/signup')
        self.assertEquals(response.status_code, 200)
        with self.client:
            response = self.client.post('/signup',
                    data=dict(username='test_user', 
                    email='testuser@localh.ost',
                    password='verysecret',
                    confirm='verysecret'),
                    follow_redirects=True
                )
            self.assertEquals(response.status_code, 200)
            self.assertIn(b'Setup your new Store', response.data)

    def test_02_that_user_can_login(self):
        pass

    def test_03_that_user_can_create_store(self):
        pass

    def test_04_that_user_has_public_store_url(self):
        pass


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    if __name__ == '__main__':
        unittest.main()