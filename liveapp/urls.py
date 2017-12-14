from django.conf.urls import url
from djgeojson.views import GeoJSONLayerView
from rest_framework.urlpatterns import format_suffix_patterns


# from .feeds import LatestEventFeed
from liveapp.models import *


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^incidence', views.incidence, name='incidence'),

    url(r'^incidences_data', views.incidence_data, name='incid'),

    url(r'^corridors_data', views.CorridorList.as_view(), name='corridors'),
    url(r'^facilities_data$', views.facility_data, name='facility_data'),
    url(r'^markets_data$', views.market_data, name='market_data'),
    url(r'^events_data$', views.event_data, name='events_data'),
    url(r'^corridors$', views.corridors, name='corridors'),

    url(r'^cattle_data$', views.cattle_data, name='cattle'),
    url(r'^sheep_data$', views.sheep_data, name='sheep'),
    url(r'^goat_data$', views.goat_data, name='goat'),
    url(r'^poultry_data$', views.poultry_data, name='poultry'),

    url(r'^charts$', views.charts, name='charts'),
    url(r'^sms$', views.sms, name='sms'),

    url(r'^towns_data$', views.town_data, name='towns_data'),
    url(r'^subcounties_data$', views.subcounty_data, name='subcounty_data'),
    url(r'^maps$', views.maps, name='maps'),
    url(r'^incidence$', views.incidence, name='incidence'),




    url('^portal$', views.portal, name='portal'),
    url(r'^incidences$', views.IncidenceList.as_view()),

    url(r'^login/$', views.user_login, name='login'),




]
urlpatterns = format_suffix_patterns(urlpatterns)
