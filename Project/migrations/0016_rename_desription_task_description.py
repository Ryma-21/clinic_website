# Generated by Django 4.2 on 2024-01-21 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0015_rename_end_date_task_deadline_remove_task_start_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='desription',
            new_name='description',
        ),
    ]
