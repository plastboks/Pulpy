from pulpy.models.meta import (
    DBSession,
    Base,
)

from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    Text,
    String,
    Unicode,
    UnicodeText,
    DateTime,
    Boolean,
    ForeignKey,
    or_,
    and_,
)


from cryptacular.bcrypt import BCRYPTPasswordManager


class User(Base):
    """
    Class constants representing database table and its columns.

    id -- integer, primary key
    email -- string, unique, max 255 characters.
    givenname -- string, max 255 characters.
    surname -- string, max 255 characters.
    password -- string, bcrypt, max 255 characters.
    archived -- boolean.
    blocked -- boolean.
    updated -- datetime.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    givenname = Column(String(255))
    surname = Column(String(255))
    password = Column(String(255), nullable=False)
    archived = Column(Boolean, default=False)
    blocked = Column(Boolean, default=False)
    last_logged = Column(DateTime, default=datetime.utcnow)
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.utcnow)

    """ Class constant used for accessing Bcrypt password manager. """
    pm = BCRYPTPasswordManager()

    """ Method for returning a user based on id.

    id -- int, user id.
    """
    @classmethod
    def by_id(cls, id):
        return DBSession.query(User).filter(User.id == id).first()

    """ Method for returning a user based on email.
    We can do this, because the email column in the database is set as unique.

    email -- string, email.
    """
    @classmethod
    def by_email(cls, email):
        return DBSession.query(User).filter(User.email == email).first()

    """ Method for checking object password against string.

    password -- string.
    """
    def verify_password(self, password):
        return self.pm.check(self.password, password)
