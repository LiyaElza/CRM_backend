# Generated by Django 4.1.3 on 2022-11-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='PhoneNumber',
            field=models.BigIntegerField(),
        ),
    ]