
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def sayHello(request):
    return HttpResponse('<h1 style="color:red">welcome to new project.</h1>')

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "project1/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "project1/detail.html", {"question":question})