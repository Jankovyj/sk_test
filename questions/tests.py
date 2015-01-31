from django.test import TestCase, Client
from django.utils.translation import ugettext as _
from questions.models import Question
from django.contrib.auth.models import User
from django.core import mail

class QuestionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="TestUser", email="test@test.com",
            password="test")
        self.client.login(username="Test", password="test")
        self.questions = []
        for i in range(20):
            question = Question.objects.create(
                title="Hello %d" % i,
                text="Text ... %d" % i,
                user=self.user
            )
            self.questions.append(question)

    def test_homepage_contains_questions(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.questions[2].title, str(response.content))
        self.assertNotIn(self.questions[5].title, str(response.content))

    def test_pagination(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(_("next"), response.content.decode('utf8'))
        response = self.client.get('/?page=2')
        self.assertIn(self.questions[5].title, str(response.content))
        self.assertNotIn(self.questions[2].title, str(response.content))
        self.assertIn(_("next"), response.content.decode('utf8'))
        self.assertIn(_("previous"), response.content.decode('utf8'))

    def test_detail_question(self):
        question_id = self.questions[2].id
        response = self.client.get('/'+str(question_id)+'/')
        self.assertEquals(response.status_code, 200)
        self.assertIn(self.questions[2].text, str(response.content))

    def test_comment(self):
        self.client.login(username="TestUser", password="test")
        question_id = self.questions[3].id
        response = self.client.post('/'+str(question_id)+'/', 
                                    {'comment_text': 'answer for question'})
        response = self.client.get('/'+str(question_id)+'/')
        self.assertIn('answer for question', str(response.content))
        self.client.logout()
        response = self.client.post('/'+str(question_id)+'/', 
                                    {'comment_text': '2 answer for question'})
        response = self.client.get('/'+str(question_id)+'/')
        self.assertNotIn('2 answer for question', str(response.content))
    
