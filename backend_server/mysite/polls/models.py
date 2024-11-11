from django.db import models
import datetime
from django.utils import timezone
class Question(models.Model):
    ques_txt = models.CharField(max_length=50)
    publish_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.ques_txt
    
    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_txt
