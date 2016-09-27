from django.shortcuts import render

from .models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
