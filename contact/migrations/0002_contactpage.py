# Generated by Django 2.1.7 on 2019-05-25 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('h_one', models.CharField(default='H1', max_length=250)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
