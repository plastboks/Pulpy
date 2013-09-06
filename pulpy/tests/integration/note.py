from webtest import TestApp
from pulpy.tests.integration import IntegrationTestBase
from pulpy.tests.integration import _initTestingDB


class IntegrationNoteViews(IntegrationTestBase):

    def setUp(self):
        self.app = TestApp(self.app)
        self.session = _initTestingDB(maketwousers=True)

    def tearDown(self):
        del self.app
        self.session.remove()

    def test_notes(self):
        # login
        res = self.app.get('/login')
        token = res.form.fields['csrf_token'][0].value
        res = self.app.post('/login', {'submit': True,
                                       'csrf_token': token,
                                       'email': 'user1@email.com',
                                       'password': '1234567'}
                            )

        # check index page
        res = self.app.get('/')
        self.assertTrue(res.status_int, 200)
        self.assertTrue('My notes', res.body)

        #create a new note
        res = self.app.get('/note/new')
        self.assertTrue('New note', res.body)
        token = res.form.fields['csrf_token'][0].value
        res = self.app.post('/note/new', {'title': 'testnote',
                                          'body': 'hello world',
                                          'csrf_token': token}
                            )

        # check for note in list
        res = self.app.get('/')
        self.assertTrue('testnote', res.body)
        
        # view the note
        res = self.app.get('/note/view/1')
        self.assertIn('hello world', res.body)

        # edit the note and create a new revision
        res = self.app.get('/note/edit/1')
        self.assertTrue('testnote', res.body)
        token = res.form.fields['csrf_token'][0].value
        res = self.app.post('/note/edit/1', {'title': 'notetest',
                                             'id': 1,
                                             'body': 'bye cruel world',
                                             'csrf_token': token}
                            )
        # view the first revision
        res = self.app.get('/note/edit/1?revision=1')

        # try to view a none existing revision or someone elses
        res = self.app.get('/note/edit/1?revision=100')
        self.assertTrue('bye cruel world',
                        res.form.fields['body'][0].value
                        )

        # try to edit none existing note
        res = self.app.get('/note/edit/100', status=404)
        # try to view a none existing note
        res = self.app.get('/note/view/100', status=404)

        # logout
        self.app.get('/logout')

        # login with the other user
        res = self.app.get('/login')
        token = res.form.fields['csrf_token'][0].value
        res = self.app.post('/login', {'submit': True,
                                       'csrf_token': token,
                                       'email': 'user2@email.com',
                                       'password': '1234567'}
                            )

        res = self.app.get('/', status=200)
        self.assertTrue('My notes', res.body)
        self.assertTrue('No notes found', res.body)

        # try to edit a note the user do not have permission to edit
        self.app.get('/note/edit/1', status=403)
        # try to view a note the user do not have permission to view
        self.app.get('/note/view/1', status=403)
