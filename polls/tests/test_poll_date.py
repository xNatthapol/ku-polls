"""Tests of poll date."""
import datetime
from django.test import TestCase
from django.utils import timezone
from polls.models import Question


class PollDateTest(TestCase):
    """Tests of poll date."""
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True
        for questions whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_future_pub_date(self):
        """
        is_published() should return False
        if the question has a future pub_date.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_pub_date = Question(pub_date=time)
        self.assertIs(future_pub_date.is_published(), False)

    def test_default_pub_date(self):
        """
        is_published() should return True
        if the question has a default pub_date (now).
        """
        time = timezone.now()
        default_pub_date = Question(pub_date=time)
        self.assertIs(default_pub_date.is_published(), True)

    def test_past_pub_date(self):
        """
        is_published() should return True
        if the question has a past pub_date.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        past_pub_date = Question(pub_date=time)
        self.assertIs(past_pub_date.is_published(), True)
