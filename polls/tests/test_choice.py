"""Tests of Choice."""
import datetime
from django.utils import timezone
from django.test import TestCase
from polls.models import Question, Choice


class ChoiceTest(TestCase):
    """Tests of Choice."""
    def test_add_choice(self):
        """Test adding a choice to a question."""
        time = timezone.now() + datetime.timedelta(days=-5)
        # Create a question
        question = Question.objects.create(
            question_text="Question test 001", pub_date=time)
        # Create a choice
        choice = Choice.objects.create(
            question=question, choice_text="choice test 001")

        # Check that the choice was created
        self.assertEqual(question.choice_set.count(), 1)
        self.assertEqual(choice.choice_text, "choice test 001")
