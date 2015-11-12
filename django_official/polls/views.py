from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    # questions = Question.objects.all()
    template = 'index.html'
    context = {'questions': questions}
    return render(request, template, context)


def detail(request, question_id):
    return HttpResponse('Your looking at question ' + question_id)


def results(request, question_id):
    return HttpResponse('Your looking at results of ' + question_id)


def vote(request, question_id):
    return HttpResponse('Your voting at ' + question_id)
