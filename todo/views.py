from django.shortcuts import render, redirect
from django.http import HttpResponse


def create_session(request):
    request.session['name'] = 'username'
    return HttpResponse("<h1>Welcome. Please refresh the page. I hope to enjoy the todo app.</h1>" + "<a href='/'>Click here</a>")


def access_session(request):
    response = 'index/'
    if request.session.get('name'):
        return redirect(response)
    else:
        return redirect('create/')
