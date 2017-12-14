from django.contrib import admin
from liveapp.models import *
from django.contrib.gis import admin as geoadmin
from leaflet.admin import LeafletGeoAdmin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class IncidenceAdmin(geoadmin.OSMGeoAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'sub_county', 'date_reported', 'animal', 'disease')
    search_fields = ['first_name', 'email']
    ordering = ['id']
    #readonly_fields = ['dc_comments ','upload_dcreport', 'final_comments']
    #filter_horizontal = ('authors',)
    list_filter = ('id', 'disease',)
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class CorridorAdmin(geoadmin.OSMGeoAdmin):
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class ManureAdmin(geoadmin.OSMGeoAdmin):
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class CattleAdmin(geoadmin.OSMGeoAdmin):
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class GoatAdmin(geoadmin.OSMGeoAdmin):
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class SheepAdmin(geoadmin.OSMGeoAdmin):
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class PoultryAdmin(geoadmin.OSMGeoAdmin):
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class MarketAdmin(geoadmin.OSMGeoAdmin):
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class EventAdmin(geoadmin.OSMGeoAdmin):
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class SubcountyAdmin (geoadmin.OSMGeoAdmin):
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class FacilityAdmin (geoadmin.OSMGeoAdmin):
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


class TownAdmin (geoadmin.OSMGeoAdmin):
    list_display = ('town_name', )
    search_fields = ['town_name', ]
    ordering = ['town_name', ]
    default_lon = 4124488.98858  # 37.050093#
    default_lat = -62466.02641  # -0.561360
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500


admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(Corridor, CorridorAdmin)
admin.site.register(Manure, ManureAdmin)
admin.site.register(Cattle, CattleAdmin)
admin.site.register(Goat, GoatAdmin)
admin.site.register(Sheep, SheepAdmin)
admin.site.register(Poultry, PoultryAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Market, MarketAdmin)
admin.site.register(Event, EventAdmin)


admin.site.register(Subcounty, SubcountyAdmin)
admin.site.register(Town, TownAdmin)
