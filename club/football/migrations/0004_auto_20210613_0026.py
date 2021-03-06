# Generated by Django 3.2.3 on 2021-06-13 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0003_auto_20210611_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubmember',
            name='profile_pic',
            field=models.URLField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='playgrounds',
            name='photo',
            field=models.URLField(max_length=255, null=True),
        ),
    ]
