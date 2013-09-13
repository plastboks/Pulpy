from webtest import TestApp
from pulpy.tests.integration import IntegrationTestBase
from pulpy.tests.integration import _initTestingDB


class IntegrationBasicViews(IntegrationTestBase):

    def setUp(self):
        self.app = TestApp(self.app)
        self.session = _initTestingDB(makeuser=True)

    def tearDown(self):
        del self.app
        self.session.remove()

    def test_404_page(self):
        res = self.app.get('/3orej23riojwefiljw', status=200)
        self.assertIn('404 - Page not found', res.body)

    def test_403_page(self):
        res = self.app.get('/note/edit/1', status=302)
