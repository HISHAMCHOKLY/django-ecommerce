# Generated by Django 2.2.12 on 2022-12-20 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='p_total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
