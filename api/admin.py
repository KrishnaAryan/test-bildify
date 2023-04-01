from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'user', 'date')
    list_filter = ('user', 'date')
    search_fields = ('title', 'description')
    readonly_fields = ('user', 'date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()