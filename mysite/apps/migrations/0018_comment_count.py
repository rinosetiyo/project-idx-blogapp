# Generated by Django 5.0 on 2024-11-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0017_remove_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
