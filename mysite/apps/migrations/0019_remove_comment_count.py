# Generated by Django 5.0 on 2024-11-07 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0018_comment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='count',
        ),
    ]
