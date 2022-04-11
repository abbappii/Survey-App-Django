from unicodedata import name
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

from . import views
urlpatterns = [ 

    path('home/',views.indexPage, name = 'homepage'),
    path('login/', auth_views.LoginView.as_view(template_name="admin/login.html"), name='login'),

    path('',login_required(TemplateView.as_view(template_name="surveys/list.html")),name='survey'),

    path('<int:pk>/start/', TemplateView.as_view(template_name="surveys/questions.html")),

    
    path('question/answer/list/', views.AnswerListAPIView.as_view()),

    path('question/list/', views.QuestionListAPIView.as_view()),
    
    path('list/', views.SurveyListAPIView.as_view()),
]