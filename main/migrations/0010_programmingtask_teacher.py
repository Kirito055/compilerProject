# Generated by Django 2.2.8 on 2022-05-23 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_teacher_uniquenumber'),
        ('main', '0009_programmingtasksolution_isplagiarized'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingtask',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Teacher'),
        ),
    ]
