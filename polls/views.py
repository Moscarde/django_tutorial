from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    context = {"latest_question_list": latest_question_list}

    # # Utilizando HttpResponse
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))

    # Utilizando render
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "Você está olhando para os resultados das questões %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s" % question_id)
