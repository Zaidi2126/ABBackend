# Generated by Django 4.1.4 on 2023-06-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessorie', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image_urls',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
