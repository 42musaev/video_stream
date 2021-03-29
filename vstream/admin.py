from django.contrib import admin

from vstream.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
