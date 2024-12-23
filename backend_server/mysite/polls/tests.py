from django.test import TestCase
import datetime
from .models import Question
from django.utils import timezone
from django.urls import reverse

# Create your tests here.

class QuestionModelTests(TestCase):
    def test_was_pub_recently_with_future_ques(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(ques_txt="future ques", publish_date=time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_pub_recently_with_old_ques(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(ques_txt="old ques", publish_date=time)
        self.assertIs(old_question.was_published_recently(), False)
    
    def test_was_pub_recently_with_recent_ques(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59,seconds=59)
        rec_question = Question(ques_txt="recent ques", publish_date=time)
        self.assertIs(rec_question.was_published_recently(), True)

class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, "No Polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])