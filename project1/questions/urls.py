from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-random-question/', views.get_random_question, name='get_random_question'),
    path('check-answer/', views.check_answer, name='check_answer'),
]