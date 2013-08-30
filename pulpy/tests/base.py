import unittest
import cgi
import transaction

from pyramid import testing
from webtest import TestApp
from webtest import Upload
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cryptacular.bcrypt import BCRYPTPasswordManager as BPM

from webob import multidict

from pulpy import main
from pulpy.models.meta import DBSession, Base
from pulpy.models import (
    User,
)



class BaseTestCase(unittest.TestCase):
    """ Base class used for all unittests. This sets up the.
    database and so forth.
    """
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite://')

    def setUp(self):
        Base.metadata.create_all(self.engine)
        DBSession.configure(bind=self.engine)
        self.session = DBSession
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()
        self.session.remove()
