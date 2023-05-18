from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)


class Galleries(admin.TabularInline):
    model = Image

class Characteristic(admin.TabularInline):
    model = Characteristics

class ProductUtils(admin.ModelAdmin):
    inlines = [Galleries, Characteristic]
    list_display = ['id', 'get_html_photo', 'name']

    def get_html_photo(self, obj):
        first_image = obj.images.first()
        if first_image:
            return mark_safe(f"<img src='{first_image.image.url}' width='50'>")
        return "-"

admin.site.register(Product, ProductUtils)
admin.site.register(Category)
admin.site.register(SubCategory)