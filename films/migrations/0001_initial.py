# Generated by Django 2.2.1 on 2019-05-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movieid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]