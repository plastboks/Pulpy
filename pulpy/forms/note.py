from pulpy.forms.meta import BaseForm, strip_filter

from wtforms import (
    validators,
    TextField,
    TextAreaField,
    HiddenField,
    PasswordField,
    BooleanField,
)


class NoteCreateForm(BaseForm):
    """
    Class constants representing form fields.

    title -- category tilte
    private -- category boolean field
    """
    title = TextField('Title',
                      [validators.Length(min=3, max=255)],
                      filters=[strip_filter])
    body = TextAreaField('Body')

class NoteEditForm(NoteCreateForm):
    """
    Class constants representing form fields.

    id -- category id, used in edit forms.
    """
    id = HiddenField()
