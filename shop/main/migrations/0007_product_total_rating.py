# Generated by Django 4.0.1 on 2022-02-08 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_sale_alter_review_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_rating',
            field=models.IntegerField(null=True),
        ),
    ]