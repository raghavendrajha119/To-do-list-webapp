# Generated by Django 4.2.3 on 2023-10-14 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_note_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='priority',
            new_name='Priority',
        ),
    ]
