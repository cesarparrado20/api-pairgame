from django.contrib import admin

from worlds.models import World, Image


@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_display_links = ["name", "description"]
    search_fields = ["name"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "world", "consultation_data"]
    list_display_links = ["title", "world", "consultation_data"]
    search_fields = ["title"]
    list_filter = ["world"]
