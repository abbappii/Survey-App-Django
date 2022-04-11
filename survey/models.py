from importlib.metadata import requires
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Survey(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    start_time = models.TimeField()
    end_time = models.TimeField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    TEXT = 'text'
    RADIO = 'radio'
    SELECT_MULTIPLE_CHECKBOX = 'Checkbox List'

    Question_choice = (
        (TEXT, 'text'),
        (RADIO, 'radio'),
        (SELECT_MULTIPLE_CHECKBOX, 'Checkbox List'),
    )

    survey = models.ForeignKey(Survey,on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=200, blank=False)
    question_type = models.CharField(max_length=20, choices=Question_choice)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'survey',)       



class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='answers', null=True, blank=True)
    answer = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

