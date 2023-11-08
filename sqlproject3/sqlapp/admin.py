from django.contrib import admin
from sqlapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
	list_display=['eno','name','salary','exp']
admin.site.register(Employee,EmployeeAdmin)
# Register your models here.
