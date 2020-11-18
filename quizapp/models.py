from django.db import models
import random
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.utils.translation import gettext as _



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.IntegerField(blank=True, null=True)

    s = 0

    def update_score(self):
        global s
        self.total_score +=  s
        self.save()

    def __str__(self):
        return f'<Profile: user={self.user}>'



class Question(models.Model):
    questionid = models.IntegerField(primary_key=True, default="", editable=False)
    question = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    imagefield = models.TextField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    n_answer = models.IntegerField(blank=True, null=True)
    n_image = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    id = models.IntegerField(primary_key=True, default="", editable=False)
    questionid = models.IntegerField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    definition = models.TextField(blank=True, null=True)

class image(models.Model):
    #id = models.IntegerField(primary_key=True, default="", editable=False)
    name = models.IntegerField(blank=True, null=True)
    describtion = models.TextField(blank=True, null=True)
    mode = models.CharField(max_length=255)
    celltype = models.CharField(max_length=255)
    component = models.CharField(max_length=255)
    doi = models.CharField(max_length=255)
    organism = models.CharField(max_length=255)
