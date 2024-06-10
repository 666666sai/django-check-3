from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if (request.GET):
        data=request.GET['userText']
    else:
        data=' '
    return render(request, "home.html",{'KEY':data})