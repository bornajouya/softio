# Generated by Django 3.2 on 2021-06-11 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatAPI', '0005_alter_chat_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 16, 55, 53, 858055)),
        ),
    ]
