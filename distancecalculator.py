"""
Contains two functions. distcalc takes a list of lists and a tuple. The tuple
contains two coordinates on a sphere and each list item contains a location
name and its coordinates on the same sphere. For each item in the list the
function attempts to float the coordinates. If it fails it will feed a
apValueError into the errorhandler function and return the result. Otherwise
it will feed the coordinates for each list item and coordinates from the tuple
into the haversineform function which will return the distance between them.
The function will then return the list item with the shortest distance from the
tuple along with the distance.
The second function haversineform takes four floats as arguements comprising two
sets of coordinates before converting them into radians. Then finds the delta
between the longitude and latidue of the first coordinate and longitude and
latidue of the second. Once calculated it uses the Harversine formula to first
calculate the square of half the chord length between the two points as a, then
the angular distance in radians as c. Then multiplying the angular distance
with the radius of the sphere in kilometers to return the distance between the
two sets of coordinates.
"""

from math import radians, cos, sin, asin, sqrt
from errorhandler import errorhandler

def distcalc(airports,coordinates):
    """Takes a list of lists and a tuple. The tuple contains two coordinates on
    a sphere and each list item contains a location name and its coordinates on
    the same sphere. For each item in the list the function attempts to float
    the coordinates. If it fails it will feed an apValueError into the
    errorhandler function and return the result. Otherwise it will feed the
    coordinates for each list item and coordinates from the tuple into the
    haversineform function which will return the distance between them. The
    function will then return the list item with the shortest distance from the
    tuple along with the distance.
    """
    lat = coordinates[0]
    lon = coordinates[1]
    dist = []
    for row in airports:
        try:
            airportlat = float(row[2])
            airportlon = float(row[3])
        except ValueError:
            return errorhandler("apValueError")
        dist.append(haversineform(lat, airportlat, lon, airportlon))
    nearestport = airports[dist.index(min(dist))]
    return nearestport, round(min(dist),2)

def haversineform(lat1, lat2, lon1, lon2):
    """Takes four floats as arguements comprising two sets of coordinates before
    converting them into radians. Then finds the delta between the longitude and
    latidue of the first coordinate and longitude and latidue of the second.
    Once calculated it uses the Harversine formula to first calculate the
    square of half the chord length between the two points as a, then the
    angular distance in radians as c. Then multiplying the angular distance
    with the radius of the sphere in kilometers to return the distance between
    the two sets of coordinates.
    """
    lat1, lat2, lon1, lon2 = map(radians, [lat1, lat2, lon1, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2 # a is the square of half the chord length between two points
    c = 2 * asin(sqrt(a)) # angular distance in radians
    r = 6371 # Radius of earth in kilometers.
    return c * r
