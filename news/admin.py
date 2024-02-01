from django.contrib import admin
from .models import News, Sport

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    search_fields = ['id', 'title']
    ordering = ['-id']

admin.site.register(News, NewsAdmin)
class SportAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'slug']
    search_fields = ['title', 'category']

admin.site.register(Sport, SportAdmin)