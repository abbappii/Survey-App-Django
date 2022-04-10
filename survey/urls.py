from django.urls import path

from . import views

urlpatterns = [ 
    path('test/',views.test, name = 'test'),
    path('',views.get, name='get_survey'),
    path('answer/', views.post, name = 'user_answer'),
]