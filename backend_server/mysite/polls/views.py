from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
# Create your views here.


def index(request):
    questions = Question.objects.all()
    # template = loader.get_template("polls/index.html")
    context = {
        'latest_question_list': questions
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

# http://127.0.0.1:8000/polls/1/
def detail(request, ques_id):
    # ques_id passed as 1
    # I am writing -> Select ques_txt from Question where id=ques_id
    # try:
    #     q = Question.objects.get()
    #     ques_text = q.ques_txt
    # except Question.DoesNotExist:    
    #     raise Http404("Question does not exist")
    
    question = get_object_or_404(Question,pk=ques_id)
    context = {
        'question': question
    }
    # return HttpResponse("You are looking at question %s."% question.ques_txt)
    return render(request,"polls/detail.html", context)

# http://127.0.0.1:8000/polls/1/results/
def results(request, ques_id):
    return HttpResponse("You are looking at the results of question %s."%ques_id)

# http://127.0.0.1:8000/polls/1/vote/
def vote(request, ques_id):
    question = get_object_or_404(Question,pk=ques_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {"question":question, "error_message": "You didn't Select a valid choice"})
    else:
        selected_choice.votes = F("votes") + 1 # Tells the database to increment the count by 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))