# Generated by Django 2.0.3 on 2018-03-15 08:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2018, 3, 15, 8, 14, 11, 371493, tzinfo=utc)),
            preserve_default=False,
        ),
    ]