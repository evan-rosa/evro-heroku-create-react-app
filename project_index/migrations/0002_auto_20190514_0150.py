# Generated by Django 2.1.7 on 2019-05-14 01:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailforms', '0003_capitalizeverbose'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('project_index', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectPage',
            new_name='ProjectIndexPage',
        ),
    ]
