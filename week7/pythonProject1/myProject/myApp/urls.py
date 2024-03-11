from django.urls import path
from . import views

urlpatterns = [
    path('q1', views.ques1, name='ques1'),
    path('q2', views.ques2, name='ques2'),
    path('find_people', views.find_people, name='find_people'),
    path('q4', views.ques4, name='ques4'),
    path('q4form', views.q4form, name='ques4form'),
    path('q5', views.index, name='index'),
    path('update/<int:human_id>/', views.update_human, name='update_human'),
    path('delete/<int:human_id>/', views.delete_human, name='delete_human'),

]