# Generated by Django 4.2.2 on 2023-06-28 23:58

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questao",
            name="resposta",
            field=smart_selects.db_fields.ChainedForeignKey(
                chained_field="pergunta",
                chained_model_field="pergunta",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.resposta",
            ),
        ),
    ]