# Generated by Django 4.1.3 on 2023-04-27 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravand', '0003_remove_ravand_image_remove_ravand_routin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesravand',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='home/ravand/'),
            preserve_default=False,
        ),
    ]
