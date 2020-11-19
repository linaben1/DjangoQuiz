# Generated by Django 3.1.2 on 2020-11-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionid', models.IntegerField(default='', editable=False, primary_key=True, serialize=False)),
                ('question', models.TextField(blank=True, null=True)),
                ('type', models.TextField(blank=True, null=True)),
                ('imagefield', models.TextField(blank=True, null=True)),
                ('point', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]