# Generated by Django 3.1.2 on 2020-11-16 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0014_auto_20201115_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='total_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]