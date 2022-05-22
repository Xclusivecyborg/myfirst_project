
from django.urls import path
from .views import aboutMe, contactMe, myProjects

urlpatterns = [
    path('', aboutMe),
    path('contactme/', contactMe),
    path('myprojects/', myProjects),
]
