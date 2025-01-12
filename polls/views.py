from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("Você está olhando para a questão %s." % question_id)

def results(request, question_id):
    response = "Você está olhando para os resultados das questões %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s" % question_id)