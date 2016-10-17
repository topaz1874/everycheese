from django.contrib import admin

# Register your models here.
from .models import WarehouseItem, Trans

admin.site.register(Trans)

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
admin.site.register(WarehouseItem, WarehouseAdmin)
