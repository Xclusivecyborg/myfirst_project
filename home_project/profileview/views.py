from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def aboutMe(request):
    return render(request, 'profileview/profile.html')

def contactMe(request):
    return render(request, 'profileview/contact.html')

def myProjects(request):
    return render(request, 'profileview/projects.html')
 