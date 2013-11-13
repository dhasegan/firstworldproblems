# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    if request.method != 'POST':
        return render(request, 'base.html', {})
    return render(request, 'base.html', {})