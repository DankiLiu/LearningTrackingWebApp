# Generated by Django 3.2.8 on 2023-06-18 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crochetwork', '0004_auto_20230617_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_image',
            field=models.ImageField(default=None, upload_to='images/<property object at 0x7fe213a289a0>/'),
        ),
    ]