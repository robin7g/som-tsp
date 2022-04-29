import numpy as np

def select_closest(candidates, origin):
    """Return the index of the closest candidate to a given point."""
    return euclidean_distance(candidates, origin).argmin()

def euclidean_distance(a, b):
    """Return the array of distances of two numpy arrays of points."""
    return np.linalg.norm(a - b, axis=1)


def distance_on_earth(lat1, long1, lat2, long2, radius=6378.388):
    """
    Compute distance between two points on earth specified by latitude/longitude.
    The earth is assumed to be a perfect sphere of given radius. The radius defaults
    to 6378.388 kilometers. To convert to miles, divide by 1.60934
    
    Reference
    ---------
    Adopted from John D. Cook's blog post: 
    http://www.johndcook.com/blog/python_longitude_latitude/
    """
    # Convert latitude and longitude to spherical coordinates in radians.
    degrees_to_radians = np.pi / 180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1) * degrees_to_radians
    phi2 = (90.0 - lat2) * degrees_to_radians

    # theta = longitude
    theta1 = long1 * degrees_to_radians
    theta2 = long2 * degrees_to_radians
         
    # Compute spherical distance from spherical coordinates.     
    cos = (np.sin(phi1) * np.sin(phi2)* np.cos(theta1 - theta2) + 
           np.cos(phi1) * np.cos(phi2))
    arc = np.arccos(cos)
    rv = arc * radius
    return rv

def route_distance(cities):
    """Return the cost of traversing a route of cities in a certain order."""
    points = cities[['x', 'y']]
    distances = euclidean_distance(points, np.roll(points, 1, axis=0))
    return np.sum(distances)
