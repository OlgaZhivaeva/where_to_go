from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from .models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    extra = 0
    fields = ['image', 'get_preview']
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-width: {}px; max-height={}px" />', obj.image.url, 300, 200)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ['title']
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ['title', 'image', "get_preview"]
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: {}px; max-height={}px" />', obj.image.url, 300, 200)
        return ''
