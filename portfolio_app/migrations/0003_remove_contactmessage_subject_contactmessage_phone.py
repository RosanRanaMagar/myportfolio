# Generated by Django 5.0.7 on 2025-02-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_contactmessage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='subject',
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
