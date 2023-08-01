# Generated by Django 4.1.3 on 2023-02-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_remove_manager_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='admin/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='manager',
            name='types',
            field=models.CharField(choices=[('admin', 'admin'), ('Feeding', 'opratorF'), ('Wedding', 'opratorW'), ('Beauty', 'opratorB'), ('Photographic', 'opratorP'), ('Medical', 'opratorM'), ('Laboratory', 'opratorL'), ('Sports', 'opratorS')], max_length=20),
        ),
    ]