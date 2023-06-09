# Generated by Django 3.2 on 2023-04-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_snippet_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='status',
            field=models.CharField(choices=[('本社', '本社'), ('東京支店', '東京支店'), ('名古屋支店', '名古屋支店'), ('九州支店', '九州支店')], default='案件立ち上げ', max_length=20, verbose_name='進捗状況'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('本社', '本社'), ('東京支店', '東京支店'), ('名古屋支店', '名古屋支店'), ('九州支店', '九州支店')], default='本社', max_length=20, verbose_name='担当事業所'),
        ),
    ]
