# Generated by Django 4.0.5 on 2022-07-02 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='address',
            new_name='message',
        ),
    ]
