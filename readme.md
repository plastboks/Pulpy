Pulpy
=====
A pulpy kind of notebook.

Pyramid
=======
This application is based on the [Pyramid Python Webframework](http://www.pylonsproject.org/)

Description
===========
A simple app for storing notes and other useful nitbits online.

Installation
============
  * create a virtualenv (eg: `virtualenv2 venv`). Use Python2.X
  * activate virtualenv `. venv/bin/activate`
  * clone this repo into venv directory (eg: venv/Pulpy)
  * run `pip install -e .` inside Pulpy directory
  * run `initialize_pulpy_db .ini`
  * run `pserve development.ini`

Testing
=======
This app will be written with TDD. To test the app run:
  * run `nosetests .`

Branches
========
There will mainly be two branches in this repo (@github) at all times. The master and develop branch.
The master branch will be kept back featurewise of the develop branch. This is to ensure the stability of the master branch

License
=======
The Pyramid framework code is licensed under a BSD-style [PSFL](http://www.pylonsproject.org/about/license) license.
All Pulpy code is licensed under a BSD-style [PSFL](http://en.wikipedia.org/wiki/Python_Software_Foundation_License) license.

Credits
=======
  * [Pyramid framework](http://www.pylonsproject.org/)
  * [WTForms](http://wtforms.simplecodes.com/docs/1.0.4/)
  * [SQLAlchemy](http://www.sqlalchemy.org/)
  * [Open icons](http://openiconlibrary.sourceforge.net/gallery2/?./Icons/apps/knotes.png)
