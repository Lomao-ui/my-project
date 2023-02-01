from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse('Привет')

def categories(request, catid):
    if(request.POST):
        print(request.POST)

    return HttpResponse(f"<h1>статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True) #redirect - куда мы будем перенаправляться

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception): ##exception - если произошли какаие то исключение, чтобы их как то отработать
    return HttpResponseNotFound("<h1>Страницка не найдена</h1>")