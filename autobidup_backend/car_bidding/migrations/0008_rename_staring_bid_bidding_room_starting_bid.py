# Generated by Django 4.1.7 on 2023-04-01 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_bidding', '0007_bidding_car_room_id_bidding_room_room_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bidding_room',
            old_name='staring_bid',
            new_name='starting_bid',
        ),
    ]
