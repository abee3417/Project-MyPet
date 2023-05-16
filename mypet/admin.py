from django.contrib import admin
from .models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    search_fields = ['detail']

admin.site.register(Photo, PhotoAdmin)