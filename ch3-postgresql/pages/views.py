from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    """defines the home page"""
    return render(request, 'home.html')