# Generated by Django 4.0.5 on 2022-06-07 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptop_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('ram', models.CharField(max_length=20)),
                ('rom', models.CharField(max_length=20)),
                ('HDD', models.CharField(max_length=30)),
                ('SSD', models.CharField(max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
    ]
