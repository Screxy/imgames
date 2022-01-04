from django.contrib import admin
from organizations.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subdomain', 'prefix')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'subdomain', 'prefix')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['subdomain']
        else:
            return []
