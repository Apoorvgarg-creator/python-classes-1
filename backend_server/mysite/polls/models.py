from django.db import models
import datetime
from django.utils import timezone

# One to Many Relationship --> 1 Question -> MANY CHOICES
class Question(models.Model):
    ques_txt = models.CharField(max_length=50)
    publish_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.ques_txt
    
    # Can you see what is wrong in this ?
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now
                                    
class Choice(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_txt
