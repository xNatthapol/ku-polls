"""Tests of voting."""
import datetime
from django.test import TestCase
from django.utils import timezone
from polls.models import Question


class VotingTest(TestCase):
    def test_cannot_vote_after_end_date(self):
        """
        can_vote() should return False if the question has an end_date in the past.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        end_date_in_past = Question(end_date=time)
        self.assertIs(end_date_in_past.can_vote(), False)

    def test_can_vote_before_end_date(self):
        """
        can_vote() should return True if the question has an end_date in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        end_date_in_future = Question(end_date=time)
        self.assertIs(end_date_in_future.can_vote(), True)

    def test_can_vote_if_no_end_date(self):
        """
        can_vote() should return True if the question has no end_date (end_date is null).
        """
        no_end_date = Question(end_date=None)
        self.assertIs(no_end_date.can_vote(), True)

    def test_cannot_vote_if_end_date_is_now(self):
        """
        can_vote() should return False if the question has an end_date that is now.
        """
        time = timezone.now()
        end_date_is_now = Question(end_date=time)
        self.assertIs(end_date_is_now.can_vote(), False)
