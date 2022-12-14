# Generated by Django 4.0.6 on 2022-08-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_order_tags_products_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('delivered', 'delivered')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('InDoor', 'InDoor'), ('Out Door', 'OutDoor')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
