from django.contrib import admin

# Register your models here.
from .models import WarehouseItem, Trans

# class TransAdmin(admin.ModelAdmin):
    # def save_model(self, request, obj, form, change):
    #     obj.item.amount +=  obj.trans_amount
    #     obj.item.save()
    #     obj.save()        

admin.site.register(Trans)



class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
admin.site.register(WarehouseItem, WarehouseAdmin)
