from django.shortcuts import render,HttpResponse

# generate a function that render httpresponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
