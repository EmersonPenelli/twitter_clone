from django.contrib import admin

from .models.user_model import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)