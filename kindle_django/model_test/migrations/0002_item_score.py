# Generated by Django 3.2 on 2022-12-20 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
