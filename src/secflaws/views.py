from django.http import HttpResponse
from .models import Secret
from django.shortcuts import render

def index(request):
    alphabetic_secret_list = Secret.objects.order_by('secret')
    context = {
        'alphabetic_secret_list': alphabetic_secret_list,
    }
    return render(request, 'secflaws/index.html', context)

def secret(request, secret_id):
    return HttpResponse("Someone has the following secret: %s" % secret_id)

def results(request, secret_id):
    response = "You're looking at the results of secret %s."
    return HttpResponse(response % secret_id)

    # jatka https://docs.djangoproject.com/en/3.1/intro/tutorial04/