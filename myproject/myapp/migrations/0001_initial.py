# Generated by Django 4.1 on 2022-08-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VnModel',
            fields=[
                ('vn2id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=100)),
                ('Age', models.IntegerField()),
                ('DOJ', models.DateField()),
                ('DOG', models.DateField()),
                ('Dojob', models.DateField()),
            ],
        ),
    ]