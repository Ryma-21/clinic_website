# Generated by Django 4.2 on 2024-01-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0018_alter_task_assigned_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(),
        ),
    ]
