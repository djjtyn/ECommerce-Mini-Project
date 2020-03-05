from django.shortcuts import render

def index(request):
    """This displays the index page"""
    return render(request, 'index.html')
