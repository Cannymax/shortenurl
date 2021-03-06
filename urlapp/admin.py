from django.contrib import admin

from .models import ShortUrl, ShortIndex


class ShortIndexAdmin(admin.ModelAdmin):
    readonly_fields = ('seed_cnt',)
    list_display = ('id', 'seed_cnt')


class ShortUrlAdmin(admin.ModelAdmin):
    readonly_fields = ('seed', 'short_url')
    list_display = ('id', 'seed', 'short_url', 'url')

    # def save_model(self, request, obj, form, change):
    #     obj.save()
    #     if obj.id is not None:
    #         obj.short_url = short_url.encode_url(obj.id)
    #         obj.save()


admin.site.register(ShortIndex, ShortIndexAdmin)
admin.site.register(ShortUrl, ShortUrlAdmin)
