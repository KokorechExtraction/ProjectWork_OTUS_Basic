from django.contrib import admin

from chat_app.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient", "body",)

    ordering = ("sender", "recipient", "created_at",)
    list_filter = ("sender", "recipient", "created_at",)
    search_fields = ("sender", "recipient", "created_at",)
    search_help_text = "Введите слово для поиска"

    fields = ("sender", "recipient", "body",)

