from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    """
    View for the index page.
    """
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    """
    View for the detail page.
    """
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
    def get(self, request, *args, **kwargs):
        """
        Returns the detail page for a question.
        """
        try:
            question = get_object_or_404(Question, pk=kwargs["pk"])

            if not question.can_vote():
                messages.error(request, "This page doesn't allow voting.")
                return redirect("polls:index")
        except Http404:
            messages.error(request, "This question does not exist.")
            return redirect("polls:index")
        return render(request, self.template_name, {"question": question})


class ResultsView(generic.DetailView):
    """
    View for the results page.
    """
    model = Question
    template_name = "polls/results.html"

    def get(self, request, *args, **kwargs):
        """
        Returns the results page for a question.
        """
        question = get_object_or_404(Question, pk=kwargs["pk"])
        return render(request, self.template_name, {"question": question})
        

def vote(request, question_id):
    """
    Handles voting for a particular choice in a question.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
