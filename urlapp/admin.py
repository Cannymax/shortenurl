from django.contrib import admin
from urlapp.models import ShortUrl
import short_url


class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_url', 'url')

    def save_model(self, request, obj, form, change):

        obj.save()
        if obj.id is not None:
            obj.short_url = short_url.encode_url(obj.id)
            obj.save()


admin.site.register(ShortUrl, ShortUrlAdmin)
