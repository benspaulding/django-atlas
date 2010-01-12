from django.contrib import admin

from atlas.models import Country, State, City, LocationType, Location


class AtlasBaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    search_fields = ('name', )


class StateAdmin(AtlasBaseAdmin):
    list_display = ('name', 'country')
    list_filter = ('country', )


class CityAdmin(AtlasBaseAdmin):
    list_display = ('name', 'county', 'state')
    search_fields = ('name', 'county', 'state')


class LocationAdmin(AtlasBaseAdmin):
    list_display = ('name', 'address_1', 'city', 'zip')
    list_filter = ('location_type', )
    search_fields = ('name', 'address_1', 'address_2', 'city', 'neighborhood',
        'decription')


admin.site.register(Country, AtlasBaseAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(LocationType, AtlasBaseAdmin)
admin.site.register(Location, LocationAdmin)
