# Generated by Django 4.0.4 on 2022-04-27 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_events_user_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='user_liked',
        ),
        migrations.AddField(
            model_name='events',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
