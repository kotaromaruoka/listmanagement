# Generated by Django 4.2.13 on 2024-07-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listapp", "0008_alter_taskmodel_endtime_alter_taskmodel_starttime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskmodel",
            name="progress",
            field=models.CharField(default="incomplete", max_length=100),
        ),
    ]
