# Generated by Django 4.0.4 on 2022-05-11 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackGImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageBG', models.ImageField(blank=True, upload_to='imageBG')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='teacherImages1')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='teacherImages2')),
            ],
        ),
    ]
