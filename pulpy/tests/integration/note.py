from webtest import TestApp
from pulpy.tests.integration import IntegrationTestBase
from pulpy.tests.integration import _initTestingDB


class IntegrationNoteViews(IntegrationTestBase):

    def setUp(self):
        self.app = TestApp(self.app)
        self.session = _initTestingDB(makeuser=True)

    def tearDown(self):
        del self.app
        self.session.remove()

    def test_notes(self):
        res = self.app.get('/login')
        token = res.form.fields['csrf_token'][0].value
        res = self.app.post('/login', {'submit': True,
                                       'csrf_token': token,
                                       'email': 'user@email.com',
                                       'password': '1234567'}
                            )

        res = self.app.get('/')
        self.assertTrue(res.status_int, 200)
        self.assertTrue('My notes', res.body)
