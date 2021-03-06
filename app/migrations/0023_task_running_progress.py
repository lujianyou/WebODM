# Generated by Django 2.0.3 on 2018-12-07 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20181205_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='running_progress',
            field=models.FloatField(blank=True, default=0.0, help_text="Value between 0 and 1 indicating the running progress (estimated) of this task"),
        ),
    ]
