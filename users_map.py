"""
Module to work with users locations information. And places names
Find coordinates of the stated place
Create map with twitter user locations and their user names
"""
from random import randint
import folium
import folium.plugins
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def coordinates(place: str) -> tuple[float, float]:
    """Return coordinates (latitude, longitude) of the location
    >>> coordinates('New York')
    (40.7127281, -74.0060152)
    >>> coordinates('Kyiv')
    (50.4500336, 30.5241361)
    >>> coordinates('Random Place')
    (35.25676, -80.7427)
    >>> coordinates('ornm,')
    """
    try:
        geolocator = Nominatim(user_agent="Tweet_people")
        # to handle time limits
        geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        # get geolocation information
        location = geocode(place)
        return location.latitude, location.longitude
    except AttributeError:
        return None


def create_map(users_data: dict):
    """
    Create and  map with following people locations

    :param users_data: dictionary with key: user's nickname and values - their locations

    Return: folium Map object with markers of user's locations from users_data
    """
    places_coord_dict = {}  # cached places coordinates
    # create follium map
    mmap = folium.Map(control_scale=True, location=[40, 0], zoom_start=3)
    # create folium Market cluster
    following = folium.plugins.MarkerCluster(
        name="Following people's location").add_to(mmap)
    for user, place in users_data.items():
        # if it is anew location cache it
        if place not in places_coord_dict:
            places_coord_dict[place] = coordinates(place)
        place_coords = places_coord_dict[place]
        # if place is invalid
        if not place_coords:
            continue
        # list with color choices
        colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
                  'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple',
                  'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
        # add marker of the user location to the map
        following.add_child(folium.Marker(location=[(-1)**randint(1, 2)/randint(1000, 2000) + x
            for x in place_coords], tooltip=user, icon=folium.Icon(color=colors[len(place) % 18],
                            icon_color=colors[-len(place) % 18], icon='cloud')))
    # add options to map layer
    for layer in ['cartodbdark_matter', 'Stamen Terrain', 'CartoDB positron',
                  'Stamen Toner', 'Stamen Watercolor']:
        folium.TileLayer(layer).add_to(mmap)
    mmap.add_child(folium.LayerControl())
    print(type(mmap))
    return mmap


if __name__ == '__main__':
    import get_locations
    create_map(get_locations.following_locations('Joe Biden', 10))
