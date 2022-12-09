# Generated by Django 4.1.3 on 2022-12-08 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectcrmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productstable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('thiruvalla', models.IntegerField()),
                ('kottayam', models.IntegerField()),
                ('kochi', models.IntegerField()),
                ('img', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='producttypetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producttype', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='projectcrmapptable',
        ),
        migrations.AddField(
            model_name='productstable',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectcrmapp.producttypetable', to_field='producttype'),
        ),
    ]
