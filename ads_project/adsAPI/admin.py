from django.contrib import admin
from .models import Ads


class ads_display(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_tag')
    ordering = ('id',)
    search_fields = ('title',)
    # readonly_fields = ('',)
    # fields = ('','','')


admin.site.register(Ads,ads_display)
