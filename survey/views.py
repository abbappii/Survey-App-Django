from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GetSurveySerializer
from .models import Survey, Question, Answer

@api_view(['GET'])
def get(request, *ars, **kwargs):
    qs = Survey.objects.all()
    serializer = GetSurveySerializer(qs, many=True)
    return Response(serializer.data)
# def post(request, *args, **kwargs):

