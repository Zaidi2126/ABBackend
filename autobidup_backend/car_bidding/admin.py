from django.contrib import admin
from .models import bidding_car,bidding_calender,bidding_room
# Register your models here.

class bidding_car_Admin(admin.ModelAdmin):
    list_display = ['automatic_generated_bid_id','name', 'make', 'model', 'car_type','miniform_approved']

class bidding_calender_Admin(admin.ModelAdmin):
    list_display = ['automatic_generated_bid_id','ad_title', 'bid_date', 'bid_time', 'car_type']
class bidding_room_Admin(admin.ModelAdmin):
    list_display = ['automatic_generated_bid_id','room_id', 'ad_title', 'starting_bid']


admin.site.register(bidding_car,bidding_car_Admin)
admin.site.register(bidding_calender,bidding_calender_Admin)
admin.site.register(bidding_room,bidding_room_Admin)

