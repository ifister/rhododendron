from django.contrib import admin
from rhdday.main.models import Photos
#

class PhotosAdmin(admin.ModelAdmin):
    readonly_fields = ('picture_thumb',)
    list_display = ('year', 'name_ru')
    

admin.site.register(Photos,PhotosAdmin)
