# Generated by Django 4.1.3 on 2023-08-03 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cortex', '0006_cortext_district'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cortex',
            old_name='descriptions',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='cortex',
            name='district',
        ),
    ]
