from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Survey, Question, Answer

from .serializers import AnswerSerializer, QuestionSerializer, SurveySerializer

class AnswerListAPIView(ListAPIView):

    serializer_class = AnswerSerializer
    
    def get_queryset(self):
        queryset = Answer.objects.all()
        question = self.request.query_params.get('question')
        if question is not None:
            queryset = queryset.filter(question_id=question)
        return queryset

class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        survey = self.request.query_params.get('survey')
        if survey is not None:
            queryset = queryset.filter(survey_id=survey)
        return queryset


class SurveyListAPIView(ListAPIView):

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


def indexPage(request):
    return render(request, 'index.html')