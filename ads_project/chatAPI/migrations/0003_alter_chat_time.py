# Generated by Django 3.2.3 on 2021-05-27 23:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatAPI', '0002_alter_chat_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 28, 3, 44, 9, 139886)),
        ),
    ]
