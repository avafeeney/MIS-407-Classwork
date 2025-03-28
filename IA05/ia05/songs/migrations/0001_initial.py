# Generated by Django 3.0.5 on 2020-04-09 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=100)),
                ('album', models.TextField(max_length=100)),
                ('year', models.TextField(max_length=4)),
            ],
        ),
    ]
