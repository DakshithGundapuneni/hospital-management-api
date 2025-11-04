from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Doctor

# @admin.register(Doctor)
# class DoctorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'specialization', 'op_fee', 'available_days', 'available_time')
#     search_fields = ('name', 'specialization')



@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'op_fee', 'available_time', 'available_days')
