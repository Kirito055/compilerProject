# Generated by Django 2.2.8 on 2022-05-23 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220522_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Admin'), (0, 'User'), (2, 'Teacher')], default=0),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rating', models.IntegerField(default=0)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Teacher')),
            ],
        ),
    ]
