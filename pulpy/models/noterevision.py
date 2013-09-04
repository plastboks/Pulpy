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


class Noterevision(Base):
    """
    Class constants representing database table and its columns.

    id -- integer, primary key.
    note_id -- integer, note foregin key.
    body -- string, revision body.
    archived -- boolean.
    updated -- datetime.
    created -- datetime.
    """
    __tablename__ = 'noterevisions'
    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, ForeignKey('notes.id'), nullable=False)
    body = Column(String(4096))
    archived = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.utcnow)

    """ Method for returning a user based on id.

    id -- int, user id.
    """
    @classmethod
    def by_id(cls, id):
        return DBSession.query(Noterevision)\
                        .filter(Noterevision.id == id).first()
