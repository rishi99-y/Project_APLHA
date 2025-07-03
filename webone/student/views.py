from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.
def student(request):
    long_list=[
        {'1': 'one',
         '2': 'two',
         }
    ]
    return HttpResponse(long_list)