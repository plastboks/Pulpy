Pulpy
=====

## Pulpy - The Name
The name originates from a little browsing on the interwebs for synonyms of the word "remember". A hit got to me to a synonym word site where synonyms for remember was listed. From there the route was Remember -> Mnemonic -> Nostalgic -> Mushy -> Pulpy. It might seem like a stretch, but I find the name both suiting and a bit abstract at the same time (and as a added bonus, it ends with py). So to conclude; the name is a bit abstract, but I like it.

## Pulpy - The Purpose
So what is the purpose of yet another webapp for storing information. Well but it simple, I like making webapps and I see a need for this. Document storing and transporting around has never been my strongest (or for that matter, preferred) side. This webapp is supposed to close that gap in a clean and easy way. Think of it as notes being accessible anywhere anytime (not very original...).

## Pulpy - Now and The Future
Pulpy webapp is going to be one of my long term projects, written without a final goal (seems familiar?). The reason for this is my changing needs. What seems like a good idea today, might not be needed of interest in a year, or six months. Pulpy 1.0 will only be a simple (non shared between users) app for storing private notes. Maybe in some future version, the ability for sharing notes between users will be added... who knows.

## Pulpy - The Features
Simple bulletlist follows:
* View, Create, Edit and Delete Notes.
* Syntaxhightlighting for both programming languages and LaTex code. 
* Markdown or simple wysiwyg editor.
* Tag notes for grouping and categorizing.
* Revise notes for changes and history.
* File attachments for notes.


Pyramid
=======
This application is based on the [Pyramid Python Webframework](http://www.pylonsproject.org/)

Installation
============
  * create a virtualenv (eg: `virtualenv2 venv`). Use Python2.X
  * activate virtualenv `. venv/bin/activate`
  * clone this repo into venv directory (eg: venv/Pulpy)
  * update the secret key twice in pulpy/__init__.py
  * update the secret key in pulpy/forms/meta.py
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
