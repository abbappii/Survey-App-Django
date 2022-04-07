from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from survey import serializers

from .models import Survey, Question, Answer

from .serializers import GetSurveySerializer, AnswerSerializer

@api_view(['GET'])
def get(request, *ars, **kwargs):
    qs = Survey.objects.all()
    serializer = GetSurveySerializer(qs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post(request, *args, **kwargs):

    if request.method == 'POST':
        serializer = AnswerSerializer(data = request.data)

        #  submited value validation check and save
        if serializer.is_valid(raise_exception=True):
            question = serializer.validated_data.get('question')
            answer = serializer.validated_data.get('answer')

            serializer.save()
            return Response(serializer.data)

        # if data not valid will show error stautus
        return Response({"invalid data"}, status=400)



