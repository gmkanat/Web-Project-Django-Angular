# Generated by Django 4.0.4 on 2022-04-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_likeuser_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
