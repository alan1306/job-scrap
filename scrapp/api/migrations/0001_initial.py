# Generated by Django 3.2.6 on 2021-08-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('start_date', models.CharField(max_length=20)),
                ('deadline', models.CharField(max_length=20)),
            ],
        ),
    ]
