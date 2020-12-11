from django.http import HttpResponse
from .models import Secret
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
import sqlite3
from django.db import connection


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

@login_required
def addSecret(request):
    owner_id = request.user.id
    secret = request.POST.get("secret")
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Unsafe query: risk of SQL injection
    query =  "INSERT INTO secflaws_secret (secret, owner_id) VALUES ('%s',%d) " % (secret, owner_id)
    
    cursor.execute(query)
    conn.commit()
    return redirect('/secflaws/')
