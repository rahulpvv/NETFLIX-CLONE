# Generated by Django 4.2.6 on 2023-10-29 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_rename_movie_addingcategorydb_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addingcategorydb',
            old_name='image',
            new_name='categoryimage',
        ),
    ]
