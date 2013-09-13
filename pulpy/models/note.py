from pulpy.models.meta import (
    DBSession,
    Base,
    IPP,
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
from pyramid.security import authenticated_userid
from webhelpers.paginate import PageURL_WebOb, Page


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
    current_revision = Column(Integer)
    title = Column(String(256))
    archived = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.utcnow)

    user = relationship('User', backref='notes')

    """ Method for returning a user based on id.

    id -- int, user id.
    """
    @classmethod
    def by_id(cls, id):
        return DBSession.query(Note).filter(Note.id == id).first()

    """ Method for getting notes for user.

    request -- request object.
    """
    @classmethod
    def my(cls, request):
        id = authenticated_userid(request)
        return DBSession.query(Note).filter(Note.user_id == id)

    """ Page method used for lists with pagination.

    request -- request object.
    page -- int, page int.
    """
    @classmethod
    def page(cls, request, page):
        page_url = PageURL_WebOb(request)
        return Page(Note.my(request),
                    page,
                    url=page_url,
                    items_per_page=IPP)
