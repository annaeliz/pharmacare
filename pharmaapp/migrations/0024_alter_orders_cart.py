# Generated by Django 3.2.6 on 2021-08-28 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmaapp', '0023_alter_orders_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pharmaapp.carts'),
        ),
    ]
