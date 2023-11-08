from django.contrib import admin
from sqlapp.models import Product
class productAdmin(admin.ModelAdmin):
	list_display=['pno','name','price','warenty']
admin.site.register(Product,productAdmin)
# Register your models here.
