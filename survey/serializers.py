from rest_framework import serializers

from .models import Survey, Question, Answer


class GetSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['name','description',]

