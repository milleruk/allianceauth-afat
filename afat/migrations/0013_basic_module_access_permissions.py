# Generated by Django 3.1.2 on 2020-10-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("afat", "0012_manualafat_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="AaAfat",
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
            ],
            options={
                "verbose_name": "Alliance Auth AFAT",
                "permissions": (
                    ("basic_access", "Can access the Alliance Auth AFAT module"),
                ),
                "managed": False,
                "default_permissions": (),
            },
        ),
    ]