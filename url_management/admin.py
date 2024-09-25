from django.contrib import admin
from url_management.models import ShortenedURL


@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ["name", "original_url", "shortened_url"]
