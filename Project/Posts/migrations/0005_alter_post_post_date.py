# Generated by Django 3.2.9 on 2021-12-27 19:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(default=datetime.datetime(2021, 12, 27, 21, 45, 4, 6607)),
        ),
    ]
