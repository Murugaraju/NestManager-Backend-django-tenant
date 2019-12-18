from django.shortcuts import render,HttpResponse
from .models import Sample
# Create your views here.
def sample(request):
    print(request)
    a=Sample.objects.create(name='fasdf')
    return HttpResponse('sdfsf'+str(a))