# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
import random

def home(request):
    context = {}

    if request.method == 'POST' and 'text' in request.POST and request.POST['text']:
        context['answered'] = True

        lines = []
        f = open('thirdworldproblems.txt', 'r')
        for l in f:
            lines.append( l );
        f.close()
        nrlines = len(lines)
        context['text'] = lines[ random.randint(0,nrlines-1) ]

        return render(request, 'base.html', context)

    return render(request, 'base.html', context)