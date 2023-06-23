from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page_view(request):
    """home page demo"""
    return HttpResponse('Hello world')

