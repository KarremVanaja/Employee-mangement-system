# Allows admin to manage employees visually
# list_display controls table columns


from django.contrib import admin
from .models import Employee

# Register Employee model in Django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # Columns shown in admin panel
    list_display = ('name', 'email', 'department', 'salary', 'joined_date')
