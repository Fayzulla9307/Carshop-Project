# Generated by Django 2.0 on 2018-01-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20180121_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products'),
        ),
    ]