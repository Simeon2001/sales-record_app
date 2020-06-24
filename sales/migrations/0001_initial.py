# Generated by Django 3.0.7 on 2020-06-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=15)),
                ('end_user', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=15)),
                ('model_serial_no', models.CharField(max_length=15)),
                ('qty', models.IntegerField()),
                ('gate_pass', models.CharField(max_length=15)),
                ('category', models.CharField(max_length=25)),
                ('sales_date', models.DateField()),
            ],
        ),
    ]
