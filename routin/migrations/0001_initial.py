# Generated by Django 4.1.3 on 2023-02-04 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='routin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('types', models.CharField(choices=[('skin', 'skin'), ('food', 'food')], max_length=10)),
                ('value', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('isActive', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]