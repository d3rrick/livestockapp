import os
from django.contrib.gis.utils import LayerMapping
from liveapp.models import Town

town_mapping = {
    'town_name': 'Town_Name',
    'town_type': 'Town_Type',
    'geom': 'MULTIPOINT',
}

town_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/subcounty', 'towns.shp'),)


def run(verbose=True):
    lm = LayerMapping(
        Town, town_shp, town_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
