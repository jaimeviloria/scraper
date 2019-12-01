from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display=('item_uuid','item_name')

a_rs={
        Item:ItemAdmin
        }

for o_r,a_r in a_rs.items():
    admin.site.register(o_r,a_r)

