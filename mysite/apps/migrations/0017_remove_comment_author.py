# Generated by Django 5.0 on 2024-11-07 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0016_alter_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]