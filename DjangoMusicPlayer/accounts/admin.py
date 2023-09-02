from django.contrib import admin

# Local Imports
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    pass
