import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


class QuestionModelTests(TestCase):
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
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_future_pub_date(self):
        """
        is_published() should return False if the question has a future pub_date.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_pub_date = Question(pub_date=time)
        self.assertIs(future_pub_date.is_published(), False)

    def test_default_pub_date(self):
        """
        is_published() should return True if the question has a default pub_date (now).
        """
        time = timezone.now()
        default_pub_date = Question(pub_date=time)
        self.assertIs(default_pub_date.is_published(), True)

    def test_past_pub_date(self):
        """
        is_published() should return True if the question has a past pub_date.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        past_pub_date = Question(pub_date=time)
        self.assertIs(past_pub_date.is_published(), True)

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

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns 302.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
        