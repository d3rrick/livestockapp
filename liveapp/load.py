import os
from django.contrib.gis.utils import LayerMapping
from liveapp.models import Subcounty

subcounty_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'name': 'name',
    'geom': 'MULTIPOLYGON',
}

subcounty_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data/subcounty', 'final.shp'),
)


def run(verbose=True):
    lm = LayerMapping(
        Subcounty, subcounty_shp, subcounty_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)
