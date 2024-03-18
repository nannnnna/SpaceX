from django.contrib import admin
from .models import MainContent, MenuItem, Logo, Feature

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'description')
    
class MainContentAdmin(admin.ModelAdmin):
    list_display = [ 'button_text', 'background_image', 'title_text']
admin.site.register(MenuItem)
admin.site.register(Logo)
admin.site.register(MainContent, MainContentAdmin)
