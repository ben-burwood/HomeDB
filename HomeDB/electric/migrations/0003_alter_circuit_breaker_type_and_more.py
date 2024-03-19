# Generated by Django 5.0.2 on 2024-03-19 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("electric", "0002_alter_circuit_circuit_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="circuit",
            name="breaker_type",
            field=models.CharField(
                choices=[
                    ("fuse", "Fuse"),
                    ("mcb", "MCB"),
                    ("rcd", "RCD"),
                    ("rcbo", "RCBO"),
                    ("gfci", "GFCI"),
                ],
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="circuit",
            name="current_rating",
            field=models.PositiveIntegerField(),
        ),
    ]
