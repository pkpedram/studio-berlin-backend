from django.contrib import admin
from .models import (
    Project,
    ProjectMedia,
    ProjectCategory,
    ProjectCategoryImage,
    ProjectRelatedCategory,
)

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1
    
class ProjectRelatedCategoryInline(admin.TabularInline):
    model = ProjectRelatedCategory
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'ordering', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']
    ordering = ['ordering']
    inlines = [ProjectMediaInline, ProjectRelatedCategoryInline]

class ProjectMediaAdmin(admin.ModelAdmin):
    list_display = ['media_type', 'related_project']
    list_filter = ['media_type']
    search_fields = ['related_project__name']

class ProjectCategoryImageInline(admin.TabularInline):
    model = ProjectCategoryImage
    extra = 1
    


class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at', 'updated_at']
    inlines = [ProjectCategoryImageInline]

class ProjectRelatedCategoryAdmin(admin.ModelAdmin):
    list_display = ['related_project', 'related_category', 'ordering']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMedia, ProjectMediaAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(ProjectCategoryImage)
admin.site.register(ProjectRelatedCategory, ProjectRelatedCategoryAdmin)
