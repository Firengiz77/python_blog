from django.contrib import admin

from blogs.models import Blog, Category

# Blogs index pagede slug, display column ve searchlar ucundu
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields= { 'slug': ('title',) }
    list_display = ('title','category','author','status','is_feature')
    search_fields = ('title','description','author__username')
    list_editable = ('is_feature',)


admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)