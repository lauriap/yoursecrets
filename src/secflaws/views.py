from django.http import HttpResponse
from .models import Secret
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q


@login_required
def index(request):
    secret_list = Secret.objects.filter(owner=request.user)
    context = {
        'secret_list': secret_list,
    }
    return render(request, 'secflaws/index.html', context)

# Accessible to anyone! No checks on who gets to access the data!
@login_required
def details(request, secret_id):
    secret = Secret.objects.get(pk=secret_id)
    response = "Owner: %s, secret: %s"
    return HttpResponse(response % (secret.owner.username, secret.secret))

