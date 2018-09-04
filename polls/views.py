from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    #output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse('You are looking at question %s.' % question_id)

def results(request, question_id):
    response = 'You are looking at the results of question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You`re voiting at question %s.' % question_id)