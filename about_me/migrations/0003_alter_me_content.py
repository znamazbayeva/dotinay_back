# Generated by Django 4.1.7 on 2023-04-08 18:02

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about_me', '0002_me_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='me',
            name='content',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
