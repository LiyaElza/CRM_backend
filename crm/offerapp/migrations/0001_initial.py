# Generated by Django 3.2.16 on 2022-11-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='offertable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(max_length=200)),
                ('product', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
