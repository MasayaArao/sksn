# Generated by Django 3.2 on 2023-04-19 05:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_alter_snippet_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
