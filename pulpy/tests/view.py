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
    NoteViews,
)


class BasicViewsTests(BaseTestCase):

    def test_notfound(self):
        request = testing.DummyRequest()
        m = MainViews(request)
        response = m.notfound()
        self.assertEqual(response['title'], '404 - Page not found')

    def test_login(self):
        request = testing.DummyRequest()
        request.POST = multidict.MultiDict()
        a = AuthViews(request)
        response = a.login()
        self.assertEqual(response['title'], 'Login')


class NoteViewsTest(BaseTestCase):

    def test_notes_list(self):
        request = testing.DummyRequest()
        n = NoteViews(request)
        response = n.notes()
        self.assertEqual(response['title'], 'My notes')

    def test_note_create(self):
        request = testing.DummyRequest()
        request.POST = multidict.MultiDict()
        n = NoteViews(request)
        response = n.note_create()
        self.assertEqual(response['title'], 'New note')
