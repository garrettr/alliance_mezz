from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from models import Gallery, GalleryImage

gallery_extra_fieldsets = ((None, {"fields": ("notes",)}),)

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage

class GalleryAdmin(PageAdmin):
    inlines = (GalleryImageInline,)
    fieldsets = deepcopy(PageAdmin.fieldsets) + gallery_extra_fieldsets

admin.site.register(Gallery, GalleryAdmin)
