# Generated by Django 3.2 on 2023-04-18 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_remove_fileupload_uped_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('python', 'Python'), ('ruby', 'Ruby'), ('php', 'PHP'), ('javascript', 'JavaScript')], default='python', max_length=20),
        ),
    ]
