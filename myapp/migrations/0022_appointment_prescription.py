# Generated by Django 4.0.4 on 2022-07-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_healthprofile_weights'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='prescription',
            field=models.TextField(default='not given yet'),
        ),
    ]
