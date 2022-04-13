from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    template = 'posts/index.html'
    title = 'main page'
    context = {
        'title': title,
        'text': 'это главная страница проекта anfisa'
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'groups'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)