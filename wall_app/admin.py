from django.contrib import admin
from .models import Profile, Post, Comment, Tag

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio",)
    search_fields = ("user",)
    search_help_text = "Введите слово для поиска"
    fields = ("user", "bio",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "likes_counter", "views",)

    ordering = ("author",)
    list_filter = ("author",)
    search_fields = ("author",)
    search_help_text = "Введите слово для поиска"

    fields = ("author", "content", "likes_counter", "views",)

    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    tag_list.short_description = 'Тэги'

    @admin.action(description="Увеличить likes на 100")
    def increase_likes(self, request, queryset):
        for post in queryset:
            post.rating += + 100
            post.save()

    actions = (increase_likes,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'post')
    list_filter = ('author',)
    search_fields = ('text',)

    fieldsets = (
        ('Основная информация', {
            'fields': ('text', 'author')
        }),
        ('Дополнительная информация', {
            'fields': ('post',),
            'classes': ('collapse',)
        })
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)