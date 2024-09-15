from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image', 'get_preview', 'number']
    readonly_fields = ["get_preview"]
    def get_preview(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ['get_preview']
    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))
