# Generated by Django 2.1.4 on 2019-01-02 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='people',
            new_name='Person',
        ),
    ]
