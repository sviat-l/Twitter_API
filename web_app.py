"""
MAIN MODULE create app server with to create map with following people of the user locations
Input blocks ask user to print Twitter user's nickname and number of people to be anylized
"""
from flask import Flask, render_template, request
import users_map
import get_locations

app = Flask(__name__)

# Load user home page with input blocks
@app.route("/", methods=['GET', 'POST'])
def index():
    """ load home(starting) page"""
    return render_template("starting.html")

# Load map (created html page) with users' locations
@app.route("/map", methods=['GET', 'POST'])
def map_page():
    """Create map by printed information
    load page with map with Markers"""
    # create map with parametrs: user name and number of people to show
    created_map = users_map.create_map(get_locations.following_locations(\
             request.args.get('user_name'), request.args.get('number')))
    created_map.save('templates/map.html')
    return render_template("map.html")

if __name__ == "__main__":
    app.run( host='127.0.0.1', port=8080)
