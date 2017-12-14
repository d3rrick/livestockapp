from django.forms import widgets
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from liveapp.models import *


class CorridorSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Corridor

        geo_field = "geom"
        # fields = ('id', 'time', 'number', 'geom',)
        fields = '__all__'


class IncidenceSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Incidence
        geo_field = "geom"
        fields = ('date_reported', 'sub_county', 'animal', 'disease')


class ManureSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Manure
        geo_field = "geom"
        # fields = ('route_id', 'time', 'number', 'geom',)
        fields = '__all__'
