# Generated by Django 2.1.7 on 2019-08-24 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('projects', '0014_datawine'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetWine',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('country', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('designation', models.CharField(max_length=250)),
                ('points', models.IntegerField()),
                ('price', models.IntegerField()),
                ('province', models.CharField(max_length=250)),
                ('region_1', models.CharField(max_length=250)),
                ('region_2', models.CharField(max_length=250)),
                ('variety', models.CharField(max_length=250)),
                ('winery', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='DataWine',
        ),
    ]