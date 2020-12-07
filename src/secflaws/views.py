from django.http import HttpResponse
from .models import Secret

def index(request):
    latest_secret_list = Secret.objects.order_by('secret')
    output = ', '.join([s.secret for s in latest_secret_list])
    return HttpResponse(output)

def secret(request, secret_id):
    return HttpResponse("Someone has the following secret: %s" % secret_id)

def results(request, secret_id):
    response = "You're looking at the results of secret %s."
    return HttpResponse(response % secret_id)