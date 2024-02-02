from django.contrib import admin
from .models import News, Sport, Economy, Magazine, World

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    search_fields = ['id', 'title']
    ordering = ['-id']

class SportAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'slug']
    search_fields = ['title', 'category']

class EconomyAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'slug']
    search_fields = ['title', 'category']

class MagazineAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'slug']
    search_fields = ['title', 'category']

class WorldAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'slug']
    search_fields = ['title', 'category']

admin.site.register(Economy, EconomyAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Magazine, MagazineAdmin)
admin.site.register(World, WorldAdmin)