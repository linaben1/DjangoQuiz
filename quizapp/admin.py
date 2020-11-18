from django.contrib import admin
from quizapp.models import  Question, image, Answer, Profile


admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(image)
