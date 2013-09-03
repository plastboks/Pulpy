from pulpy.forms.meta import BaseForm, strip_filter

from wtforms import (
    validators,
    TextField,
    HiddenField,
    BooleanField,
    IntegerField,
    PasswordField,
    SelectField,
)

from pulpy.models import User


class AccountEditForm(BaseForm):
    """
    Class constants representing form fields.

    email -- textfield. username.
    password -- password textfield.
    confirm -- password textfield, second confirmation.
    """
    id = HiddenField()
    email = TextField('Email',
                      [validators.Length(max=255),
                       validators.Email(message='Not an valid email address')],
                      filters=[strip_filter])
    password = PasswordField('Password',
                             [validators.Optional(),
                              validators.Length(min=6, max=128),
                              validators.EqualTo('confirm',
                                                 message='Passwords\
                                                          must match')],
                             filters=[strip_filter])
    confirm = PasswordField('Confirm password',
                            filters=[strip_filter])
