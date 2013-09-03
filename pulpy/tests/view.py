from datetime import (
    datetime,
    timedelta,
    date,
)

from pyramid import testing
from webob import multidict

from pulpy.tests import BaseTestCase

from pulpy.views import (
    MainViews,
    AuthViews,
)


class BasicViewsTests(BaseTestCase):

    def test_notfound(self):
        request = testing.DummyRequest()
        m = MainViews(request)
        response = m.notfound()
        self.assertEqual(response['title'], '404 - Page not found')

    def test_forbidden(self):
        request = testing.DummyRequest()
        m = MainViews(request)
        response = m.forbidden()
        self.assertEqual(response['title'], '403 - Forbidden')

    def test_login(self):
        request = testing.DummyRequest()
        request.POST = multidict.MultiDict()
        a = AuthViews(request)
        response = a.login()
        self.assertEqual(response['title'], 'Login')
