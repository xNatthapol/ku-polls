import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    """
    Represents a poll question.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    end_date = models.DateTimeField("date ended", null=True, blank=True)

    def is_published(self):
        """
        Returns True if the question is published.
        """
        return self.pub_date <= timezone.localtime(timezone.now())
    
    def can_vote(self):
        """
        Returns True if the question can be voted on.
        """
        return self.pub_date <= timezone.localtime(timezone.now()) \
            and ((self.end_date is None) or (self.end_date >= timezone.localtime(timezone.now())))

    def was_published_recently(self):
        """
        Returns True if the question was published within the last day.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """
    Represents a choice for a poll question.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    @property
    def votes(self):
        """Return the number count"""
        return self.vote_set.count()

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    """Record a Vote of a Choice by a User."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        pass