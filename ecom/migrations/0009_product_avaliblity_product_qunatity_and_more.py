# Generated by Django 5.0.1 on 2024-04-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_alter_customer_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avaliblity',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='qunatity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='reorderlevel',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
