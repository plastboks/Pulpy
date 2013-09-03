import transaction

from sqlalchemy import create_engine
from cryptacular.bcrypt import BCRYPTPasswordManager as BPM
from pulpy import main
from pulpy.models.meta import DBSession, Base
from pulpy.tests import BaseTestCase
from pulpy.models import User


def _initTestingDB(makeuser=False, maketwousers=False):
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
    DBSession.configure(bind=engine)
    if makeuser or maketwousers:
        m = BPM()
        hashed = m.encode(u'1234567')
        with transaction.manager:
            user = User(email=u'user1@email.com',
                        password=hashed,
                        )
            DBSession.add(user)
    if maketwousers:
        m = BPM()
        hashed = m.encode(u'1234567')
        with transaction.manager:
            user = User(email=u'user2@email.com',
                        password=hashed,
                        )
            DBSession.add(user)
    return DBSession


class IntegrationTestBase(BaseTestCase):
    @classmethod
    def setUpClass(cls):
        settings = {'sqlalchemy.url': 'sqlite://'}
        cls.app = main({}, **settings)
        super(IntegrationTestBase, cls).setUpClass()
