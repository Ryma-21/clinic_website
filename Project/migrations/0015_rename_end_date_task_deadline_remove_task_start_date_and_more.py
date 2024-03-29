# Generated by Django 4.2 on 2024-01-21 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0014_merge_0010_task_0013_alter_appointment_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='end_date',
            new_name='deadline',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start_date',
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Project.doctor'),
        ),
    ]
