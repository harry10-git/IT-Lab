from django.urls import path
from . import views

urlpatterns = [
    path('q2', views.ques2, name='ques2'),
    path('find_people', views.find_people, name='find_people'),
    path('q4', views.ques4, name='ques4'),
    path('q4form', views.q4form, name='ques4form'),

]