# Generated by Django 4.1.3 on 2022-11-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_customers_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='joiningDate',
            field=models.DateField(default=1988),
            preserve_default=False,
        ),
    ]
