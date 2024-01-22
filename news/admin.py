from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    search_fields = ['id', 'title']
    ordering = ['-id']

admin.site.register(News, NewsAdmin)