# Generated by Django 4.2.5 on 2023-09-19 23:16
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.RenameIndex(
            model_name="taggeditem",
            new_name="taggit_tagg_content_8fc721_idx",
            old_fields=("content_type", "object_id"),
        ),
    ]
