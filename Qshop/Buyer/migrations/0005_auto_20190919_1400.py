# Generated by Django 2.1.8 on 2019-09-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0004_auto_20190916_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payorder',
            name='order_status',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='order_status',
            field=models.IntegerField(default=0),
        ),
    ]
