# -*- coding: utf-8 -*-

"""
Django admin models for an atlas application.

"""

from django.contrib import admin
from atlas.models import *


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ('name', )


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country', )
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ('name', )


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'county', 'state')
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ('name', 'county', 'state')


class LocationTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('kind', )}
    search_fields = ('kind', )


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address_1', 'city', 'state', 'zip')
    list_filter = ('country', 'location_type')
    search_fields = ('name', 'address_1', 'address_2')


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(LocationType, LocationTypeAdmin)
admin.site.register(Location, LocationAdmin)
