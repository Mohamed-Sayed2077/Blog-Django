# Generated by Django 3.2.9 on 2021-12-27 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0007_alter_customer_user_date_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user_date_on',
            field=models.DateField(default=datetime.datetime(2021, 12, 27, 21, 44, 56, 474686)),
        ),
    ]
