from django.contrib import admin
from   .models import Company, Employee
# Register your models here.


# admin.site.register([Employee,Company])

# customize a model
# Customize class for Company model
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')  #how data displayed ,work like __str__ funtions 

    # Add serchbar for searching what you put in searchfields
    search_fields=('name','type')

    # Filtering data
    list_filter=('type','added_date')

# Customize class for Employee model
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Company,CompanyAdmin)