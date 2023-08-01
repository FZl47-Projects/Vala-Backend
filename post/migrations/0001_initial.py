# Generated by Django 4.1.3 on 2023-02-04 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(null=True, upload_to='', verbose_name='home/post/poster')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('like', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('isDelete', models.BooleanField()),
            ],
        ),
    ]
