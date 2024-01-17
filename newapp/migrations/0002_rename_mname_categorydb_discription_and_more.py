# Generated by Django 4.2.6 on 2023-10-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorydb',
            old_name='mname',
            new_name='discription',
        ),
        migrations.RemoveField(
            model_name='categorydb',
            name='file',
        ),
        migrations.AddField(
            model_name='categorydb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
        migrations.AddField(
            model_name='categorydb',
            name='moviename',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='categorydb',
            name='vidio',
            field=models.ImageField(blank=True, null=True, upload_to='vidios'),
        ),
    ]