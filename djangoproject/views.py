
from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter

def home(request):
    return render(request, 'index.html',{'key1':'i am from python code'})

def result(request):
    article=request.GET['article']
    vardict,wordcount=counter.count(article)

    return render(request, 'result.html', {'article': article,'wordcount': wordcount, 'dictword':vardict})
