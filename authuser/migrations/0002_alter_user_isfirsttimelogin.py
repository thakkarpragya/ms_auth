# Generated by Django 3.2.15 on 2022-08-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='isFirstTimeLogin',
            field=models.BooleanField(default=0),
        ),
    ]
