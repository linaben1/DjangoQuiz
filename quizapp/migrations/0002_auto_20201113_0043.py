# Generated by Django 3.1.2 on 2020-11-12 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='n_answer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='n_image',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]