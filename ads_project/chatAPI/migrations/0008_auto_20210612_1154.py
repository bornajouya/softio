# Generated by Django 3.2 on 2021-06-12 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatAPI', '0007_auto_20210612_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 12, 11, 54, 21, 881314)),
        ),
        migrations.DeleteModel(
            name='fk_model',
        ),
    ]
