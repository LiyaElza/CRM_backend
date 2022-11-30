# Generated by Django 4.1.3 on 2022-11-29 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectcrmapp', '0002_productstable_delete_projectcrmapptable'),
        ('reportsapp', '0002_orders_productanalysis_saleslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('ProductName', models.CharField(max_length=200)),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectcrmapp.productstable')),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportsapp.orders')),
            ],
        ),
    ]