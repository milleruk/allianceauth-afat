# Generated by Django 2.0.8 on 2018-11-13 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("afat", "0003_auto_20180911_0831"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClickAFatDuration",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("duration", models.PositiveIntegerField()),
                (
                    "fleet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="afat.AFatLink",
                    ),
                ),
            ],
        ),
    ]
