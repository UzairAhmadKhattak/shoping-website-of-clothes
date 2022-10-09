# Generated by Django 3.2.3 on 2021-06-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about_us_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employ_img', models.ImageField(upload_to='about_us_pix')),
                ('employ_name', models.CharField(max_length=50)),
                ('employ_disc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.ImageField(upload_to='galary')),
            ],
        ),
        migrations.CreateModel(
            name='home_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='home_pix')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('disc', models.TextField()),
            ],
        ),
    ]
