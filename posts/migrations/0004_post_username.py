# Generated by Django 2.0.3 on 2018-03-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180315_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
