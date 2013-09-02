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

from sqlalchemy.orm import relationship

class Note(Base):
    """
    Class constants representing database table and its columns.

    id -- integer, primary key
    last_revision -- integer
    archived -- boolean.
    updated -- datetime.
    created -- datetime.
    """
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    #last_revision = Column(Integer, ForeignKey('noterevisions.id'))
    title = Column(String(256))
    archived = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.utcnow)

    user = relationship('User', backref='notes')
    revisions = relationship('Noterevision', backref='note')

    """ Method for returning a user based on id.

    id -- int, user id.
    """
    @classmethod
    def by_id(cls, id):
        return DBSession.query(Note).filter(Note.id == id).first()
