# Generated by Django 4.2.5 on 2024-04-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_remove_customer_delete_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phone",
            field=models.BigIntegerField(),
        ),
    ]