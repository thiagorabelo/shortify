from django.contrib import admin

from .models import ShortURI

# Register your models here.


@admin.register(ShortURI)
class ShortURIAdmin(admin.ModelAdmin):
    list_display = ("uri_hash", "full_uri", "description", "user", "created_at")
    readonly_fields = ("uri_hash", )
    search_fields = ("description", "full_uri", "user__username")
