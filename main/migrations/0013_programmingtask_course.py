# Generated by Django 2.2.8 on 2022-05-23 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_chapter_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='programmingtask',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Course'),
        ),
    ]