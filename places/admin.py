from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


MAX_IMAGE_WIDTH = 300
MAX_IMAGE_HEIGHT = 200


class ImageInline(SortableStackedInline):
    model = Image
    extra = 0
    fields = ["image", "get_preview"]
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-width: {}px; max-height={}px" />', obj.image.url, MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ["title"]
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ["image", "get_preview"]
    raw_id_fields = ["title"]
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: {}px; max-height={}px" />', obj.image.url, MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT)
        return ""
