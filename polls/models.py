import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    end_date = models.DateTimeField("date ended", null=True, blank=True)

    def is_published(self):
        return self.pub_date <= timezone.localtime(timezone.now())
    
    def can_vote(self):
        return self.pub_date <= timezone.localtime(timezone.now()) \
            and ((self.end_date >= timezone.localtime(timezone.now())) or (self.end_date is None))

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
