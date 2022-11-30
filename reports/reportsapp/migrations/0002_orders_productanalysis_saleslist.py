# Generated by Django 4.1.3 on 2022-11-29 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_delete_customerorders'),
        ('projectcrmapp', '0002_productstable_delete_projectcrmapptable'),
        ('reportsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('orderid', models.IntegerField(primary_key=True, serialize=False)),
                ('orderDate', models.DateField()),
                ('amount', models.IntegerField()),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.customers')),
            ],
        ),
        migrations.CreateModel(
            name='productanalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producttype', models.CharField(max_length=20)),
                ('sales', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='saleslist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producttype', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportsapp.orders')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectcrmapp.productstable')),
            ],
            options={
                'unique_together': {('orderid', 'productid')},
            },
        ),
    ]
