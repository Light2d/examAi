# Generated by Django 5.0.1 on 2024-10-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detectedmedia',
            name='media_type',
        ),
        migrations.AlterField(
            model_name='detectedmedia',
            name='file',
            field=models.FileField(upload_to='media_files/'),
        ),
    ]