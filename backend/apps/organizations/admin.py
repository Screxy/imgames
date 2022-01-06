from django.contrib import admin
from organizations.models import Organization, OrganizationSettings


@admin.register(OrganizationSettings)
class OrganizationSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__', 'organization', 'number_of_turns_default')
    list_display_links = ('id', '__str__', 'organization')


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
