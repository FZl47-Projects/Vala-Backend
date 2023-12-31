# Generated by Django 4.1.3 on 2023-08-03 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cortex', '0005_alter_district_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='cortext_district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intensity_value', models.PositiveBigIntegerField()),
                ('cortext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cortex.cortex')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cortex.district')),
            ],
        ),
    ]
