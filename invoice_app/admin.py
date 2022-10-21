from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(invoices)
class invoicesadmin(admin.ModelAdmin):
    list_display=['id','name','address','pay_method','amount','description','order_date']