from webtest import TestApp
from pulpy.tests.integration import IntegrationTestBase
from pulpy.tests.integration import _initTestingDB


class IntegrationAccountViews(IntegrationTestBase):

    def setUp(self):
        self.app = TestApp(self.app)
        self.session = _initTestingDB(makeuser=True)

    def tearDown(self):
        del self.app
        self.session.remove()

    def test_profile(self):
        # login
        res = self.app.get('/login')
        token = res.form.fields['csrf_token'][0].value
        res = self.app.post('/login', {'submit': True,
                                       'csrf_token': token,
                                       'email': 'user1@email.com',
                                       'password': '1234567'}
                            )
        res = self.app.get('/')
        self.assertIn('My notes', res.body)

        # get profile page
        res = self.app.get('/profile', status=200)
        self.assertIn('Profile edit', res.body)
        self.assertIn('user1@email.com', res.body)

        # profile edit with password
        token = res.form.fields['csrf_token'][0].value
        res = self.app.post('/profile', {'email': 'test@email.com',
                                         'csrf_token': token,
                                         'password': 'testtest',
                                         'confirm': 'testtest',
                                         }
                            )
        # logout
        res = self.app.get('/logout')

        # login with new credentials
        res = self.app.get('/login')
        token = res.form.fields['csrf_token'][0].value
        res = self.app.post('/login', {'submit': True,
                                       'csrf_token': token,
                                       'email': 'test@email.com',
                                       'password': 'testtest'}
                            )
        res = self.app.get('/')
        self.assertIn('My notes', res.body)

        # get profile page
        res = self.app.get('/profile', status=200)
        self.assertIn('Profile edit', res.body)
        self.assertIn('test@email.com', res.body)

        # profile edit wihout password
        token = res.form.fields['csrf_token'][0].value
        res = self.app.post('/profile', {'email': 'user1@email.com',
                                         'csrf_token': token,
                                         }
                            )

        # get profile page
        res = self.app.get('/profile', status=200)
        self.assertIn('Profile edit', res.body)
        self.assertIn('user1@email.com', res.body)
