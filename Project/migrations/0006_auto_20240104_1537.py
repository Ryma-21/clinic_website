# Generated by Django 3.0.5 on 2024-01-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0005_auto_20240104_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='aid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='did',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='mid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
