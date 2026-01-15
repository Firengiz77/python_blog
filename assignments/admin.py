from django.contrib import admin

from assignments.models import About, SocialMedia


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
         return super().has_add_permission(request)
        else:
         return False

    def has_delete_permission(self, request, obj = ...):
         return False   
    

admin.site.register(About,AboutAdmin)
admin.site.register(SocialMedia)