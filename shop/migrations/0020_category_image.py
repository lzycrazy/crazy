# Generated by Django 3.2.5 on 2022-01-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='image'),
            preserve_default=False,
        ),
    ]
