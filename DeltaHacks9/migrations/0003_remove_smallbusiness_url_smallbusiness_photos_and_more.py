# Generated by Django 4.1.5 on 2023-01-15 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeltaHacks9', '0002_smallbusiness'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smallbusiness',
            name='url',
        ),
        migrations.AddField(
            model_name='smallbusiness',
            name='photos',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='smallbusiness',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
