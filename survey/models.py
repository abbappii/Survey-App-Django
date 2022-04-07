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

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


    def duration(self):
        return self.end_time - self.start_time


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

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    # user 
    question = models.ForeignKey(Question,on_delete=models.CASCADE, related_name = 'answer')
      
    answer = models.CharField(max_length=200)

    

    
