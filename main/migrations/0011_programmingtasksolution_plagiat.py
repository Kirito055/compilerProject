# Generated by Django 2.2.8 on 2022-05-23 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_programmingtask_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingtasksolution',
            name='plagiat',
            field=models.FloatField(default=0),
        ),
    ]
