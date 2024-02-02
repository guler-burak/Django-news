from django.contrib import admin
from .models import News, Sport, Economy, Magazine, World, Technology
from .models import ContactMessage
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

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image', 'slug']
    search_fields = ['title', 'category']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'urgency', 'agree_to_terms']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['urgency', 'agree_to_terms']
    list_editable = ['agree_to_terms']


admin.site.register(Economy, EconomyAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Magazine, MagazineAdmin)
admin.site.register(World, WorldAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)