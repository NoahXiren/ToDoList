# Generated by Django 5.0.7 on 2024-07-26 08:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]