# Generated by Django 2.1.7 on 2019-07-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190603_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='canonical',
            field=models.URLField(default='Canonical-URL'),
        ),
    ]
