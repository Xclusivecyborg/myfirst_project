from django.http import HttpResponse

# Create your views here.

def aboutMe(request):
    return HttpResponse("<h1> Hello, welcome to my profile. I am Ayodeji Ogundairo a full stack mobile engineer\n I build mobile apps with flutter and I am currently learning python(django) at kode camp</h1> ")  

def contactMe(request):
    return HttpResponse("<h1> You can reach me on phone via +2348030861111</h1> ")

def myProjects(request):
    return HttpResponse("<h1> I just finished building a crypto trading app for a fintech startup.</h1> \n <p><a href='https://docs.google.com/document/d/1B2mxS2yRezJGUvSQGIeyLPMWeeOCYPW1/edit'>Check out my resume here!</a></p>")
 