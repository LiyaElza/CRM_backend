# Generated by Django 4.1.3 on 2022-11-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productanalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producttype', models.CharField(max_length=20)),
                ('sales', models.IntegerField()),
            ],
        ),
    ]
