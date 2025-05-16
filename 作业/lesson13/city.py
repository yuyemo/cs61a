"""Say we have a data abstraction for cities. A city has a name, a latitude coordinate, and a longitude coordinate.

Our data abstraction has one constructor:

make_city(name, lat, lon): Creates a city object with the given name, latitude, and longitude.
We also have the following selectors in order to get the information for each city:

get_name(city): Returns the city's name
get_lat(city): Returns the city's latitude
get_lon(city): Returns the city's longitude
Here is how we would use the constructor and selectors to create cities and extract their information:

>>> berkeley = make_city('Berkeley', 122, 37)
>>> get_name(berkeley)
'Berkeley'
>>> get_lat(berkeley)
122
>>> new_york = make_city('New York City', 74, 40)
>>> get_lon(new_york)
40
All of the selector and constructor functions can be found in the lab file if you are curious to see how they are implemented. However, the point of data abstraction is that, when writing a program about cities, we do not need to know the implementation.
"""
def make_city(name,latitude,longitude):
    def city(n):
        if n==1:
            return name
        elif n==2:
            return latitude
        elif n==3:
            return longitude
    return city
def get_name(city):
    return city(1)
def get_lat(city):
    return city(2)
def get_lon(city):
    return city(3)
"""Next, implement closer_city, a function that takes a latitude, longitude, and two cities, and returns the name of the city that is closer to the provided latitude and longitude.

You may only use the selectors get_name get_lat get_lon, constructors make_city, and the distance function you just defined for this question.

Hint: How can you use your distance function to find the distance between the given location and each of the given cities?

def closer_city(lat, lon, city_a, city_b):

    Returns the name of either city_a or city_b, whichever is closest to
    coordinate (lat, lon). If the two cities are the same distance away
    from the coordinate, consider city_b to be the closer city.

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
  
    "*** YOUR CODE HERE ***"
    """
def closer_city(lat, lon, city_a, city_b):
    def distance(lat,lon,city):
        return ((get_lat(city)-lat)**2+(get_lon(city)-lon)**2)**0.5
    if distance(lat,lon,city_a)>distance(lat,lon,city_b):
        return get_name(city_b)
    else:
        return get_name(city_a)