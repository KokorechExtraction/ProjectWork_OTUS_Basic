from django.contrib import admin
from .models import CustomUser

# admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_number", "date_of_birth", "avatar", "first_name", "last_name",)

    ordering = ('username',)
    list_filter = ('username', 'email')
    search_fields = ("username", "email", "phone_number", "first_name", "last_name")
    search_help_text = "Введите слово для поиска"

    fields = ("username", "email", "phone_number", "date_of_birth", "avatar", "first_name", "last_name")
    readonly_fields = ("email",)