# Generated by Django 3.0.5 on 2024-01-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0004_auto_20240104_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='pid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
