# Generated by Django 4.2.6 on 2023-10-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(blank=True, max_length=40, null=True)),
                ('mname', models.CharField(blank=True, max_length=40, null=True)),
                ('director', models.CharField(blank=True, max_length=40, null=True)),
                ('file', models.ImageField(blank=True, max_length=40, null=True, upload_to='')),
            ],
        ),
    ]
