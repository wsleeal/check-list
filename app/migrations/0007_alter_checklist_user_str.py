# Generated by Django 4.2.2 on 2023-06-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_rename_user_checklist_user_str_checklist_user_obj"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checklist",
            name="user_str",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
