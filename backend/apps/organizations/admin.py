from django.contrib import admin
from organizations.models import Organization

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'subdomain','prefix')
    list_display_links = ('id','name')
    readonly_fields = ('subdomain',)
    search_fields = ('name', 'subdomain', 'prefix')
