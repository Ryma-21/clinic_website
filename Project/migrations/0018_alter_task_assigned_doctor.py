# Generated by Django 4.2 on 2024-01-21 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0017_alter_task_assigned_doctor_alter_task_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.doctor'),
        ),
    ]