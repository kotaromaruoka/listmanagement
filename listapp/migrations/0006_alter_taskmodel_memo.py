# Generated by Django 4.2.13 on 2024-07-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listapp", "0005_taskmodel_memo_taskmodel_progress"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskmodel",
            name="memo",
            field=models.TextField(blank=True, null=True),
        ),
    ]
