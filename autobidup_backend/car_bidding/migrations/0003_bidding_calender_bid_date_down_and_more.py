# Generated by Django 4.1.7 on 2023-04-01 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_bidding', '0002_bidding_calender'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidding_calender',
            name='bid_date_down',
            field=models.DateField(blank=True, default='2020-02-22'),
        ),
        migrations.AddField(
            model_name='bidding_calender',
            name='bid_time_down',
            field=models.TimeField(blank=True, default='00:00:00'),
        ),
    ]
