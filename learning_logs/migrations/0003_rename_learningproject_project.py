# Generated by Django 3.2.8 on 2021-10-22 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LearningProject',
            new_name='Project',
        ),
    ]
