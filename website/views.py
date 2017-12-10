
from django.shortcuts import render

def baseview(request):
    return render(request, 'homepage/homepage.html', {})