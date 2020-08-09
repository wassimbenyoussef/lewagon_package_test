
# Import from our lib
from mlproject.distance import haversine
import pytest


def test_haversine():

    lon1, lat1, lon2, lat2 = 5, 5, 10, 10

    assert haversine(lon1, lat1, lon2, lat2) == 782.7790829048026
