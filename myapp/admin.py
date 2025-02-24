from django.contrib import admin

from myapp.models import DataPoint

# Register your models here.
@admin.register(DataPoint)
class DataPointAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'sector', 'region', 'country', 'intensity', 'relevance', 'likelihood')
    search_fields = ('title', 'topic', 'sector', 'country', 'region')
    list_filter = ('sector', 'region', 'country', 'topic', 'relevance')
