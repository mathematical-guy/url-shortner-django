from django.contrib import admin
from url_management.models import ShortenedURL


@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ["created_on", "name", "original_url", ]
