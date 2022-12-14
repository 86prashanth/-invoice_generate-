# Generated by Django 4.1.1 on 2022-10-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0003_delete_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='amount',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='pay_method',
            field=models.CharField(max_length=15),
        ),
    ]
