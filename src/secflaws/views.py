from django.http import HttpResponse
from .models import Secret
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q

@login_required
def index(request):
    alphabetic_secret_list = Secret.objects.order_by('secret')
    context = {
        'alphabetic_secret_list': alphabetic_secret_list,
    }
    return render(request, 'secflaws/index.html', context)

@login_required
def secret(request, secret_id):
    return HttpResponse("Someone has the following secret: %s" % secret_id)

@login_required
def results(request, secret_id):
    response = "You're looking at the results of secret %s."
    return HttpResponse(response % secret_id)

    # jatka https://docs.djangoproject.com/en/3.1/intro/tutorial04/