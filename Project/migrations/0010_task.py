# Generated by Django 3.0.5 on 2024-01-05 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0009_remove_appointment_pre_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('desription', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
    ]
