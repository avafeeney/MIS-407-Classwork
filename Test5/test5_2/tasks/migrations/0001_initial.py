# Generated by Django 4.1.7 on 2023-11-11 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('desc', models.TextField(max_length=400)),
                ('priority', models.IntegerField(max_length=4)),
                ('done', models.BooleanField(max_length=4)),
            ],
        ),
    ]
