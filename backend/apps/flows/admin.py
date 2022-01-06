from django.contrib import admin
from .models import Flow, Card, Parameter, ParameterChange


@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'organization')
    list_display_links = ('id', 'title')


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'short_description', 'flow')
    list_display_links = ('id', 'header')


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'default_value', 'flow')
    list_display_links = ('id', 'name')


@admin.register(ParameterChange)
class ParameterChangeAdmin(admin.ModelAdmin):
    list_display = ('id', 'parameter', 'math_operator',
                    'value', 'month_of_application', 'card')
    list_display_links = ('id', 'parameter')
