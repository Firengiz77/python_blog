from django.contrib import admin

from blogs.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields= { 'slug': ('title',) }


admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)