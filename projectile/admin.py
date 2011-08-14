from django.contrib import admin

from projectile.models import ProjectCategory, Project, ProjectImage

class ProjectCategoryAdmin(admin.ModelAdmin):
    pass

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ProjectImageInline,
    ]

class ProjectImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Project, ProjectAdmin)
