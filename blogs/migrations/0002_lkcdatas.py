# Generated by Django 4.0.4 on 2022-05-11 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LKCDatas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='lkcLogo')),
                ('name', models.TextField(max_length=255)),
                ('title1', models.TextField(max_length=255)),
                ('title2', models.TextField(max_length=255)),
                ('phoneNumber', models.TextField(max_length=100)),
            ],
        ),
    ]