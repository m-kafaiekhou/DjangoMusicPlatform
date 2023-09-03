from django.contrib import admin

# Local Imports
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'email', 'status', 'is_active', )
    list_filter = ('status', 'is_active', )
    search_fields = ('first_name', 'last_name', 'username', )
    list_per_page = 20

    def display_name(self, obj):
        try:
            f_name = obj.first_name[0].upper()
            l_name = obj.last_name[0].upper() + obj.last_name[1:]
            return f'{f_name}.{l_name}'
        except IndexError:
            return 'NULL'

    display_name.short_description = 'Name'
