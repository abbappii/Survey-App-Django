from django.urls import path

from . import views

urlpatterns = [ 
    path('',views.get, name='get_survey'),
    path('answer/', views.post, name = 'user_answer'),
]