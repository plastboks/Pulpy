from cryptacular.bcrypt import BCRYPTPasswordManager as BPM
from pulpy.tests import BaseTestCase


class UserModelTests(BaseTestCase):

    def _getTargetClass(self):
        from pulpy.models import User
        return User

    def _makeOne(self, email, password, id=False):
        m = BPM()
        hashed = m.encode(password)
        if id:
            return self._getTargetClass()(id=id,
                                          email=email,
                                          password=hashed)
        return self._getTargetClass()(email=email,
                                      password=hashed,
                                      )

    def test_constructor(self):
        instance = self._makeOne(email='user1@email.com',
                                 password='1234',
                                 )
        self.assertEqual(instance.email, 'user1@email.com')
        self.assertTrue(instance.verify_password('1234'))

    def test_by_email(self):
        instance = self._makeOne(email='user2@email.com',
                                 password='1234',
                                 )
        self.session.add(instance)
        q = self._getTargetClass().by_email('user2@email.com')
        self.assertEqual(q.email, 'user2@email.com')

    def test_by_id(self):
        instance = self._makeOne(email='user3@email.com',
                                 password='1234',
                                 id=1000,
                                 )
        self.session.add(instance)
        q = self._getTargetClass().by_id(1000)
        self.assertEqual(q.email, 'user3@email.com')


class NoteModelTests(BaseTestCase):

    def _getTargetClass(self):
        from pulpy.models import Note
        return Note

    def _makeOne(self, id, title):
        return self._getTargetClass()(id=id,
                                      user_id=1,
                                      title=title,
                                      )

    def test_constructor(self):
        instance = self._makeOne(1, 'test')
        self.assertEqual(instance.title, 'test')

    def test_by_id(self):
        instance = self._makeOne(1, 'test')
        self.session.add(instance)
        q = self._getTargetClass().by_id(1)
        self.assertEqual(q.title, 'test')
