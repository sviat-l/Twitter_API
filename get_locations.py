"""
Module to work with twitter API and people locations
"""
import urllib.request
import json
import twurl

def following_locations(user:str, number:int)->dict[str:str]:
    """
    Find locations of [number] people followed on Twitter by stated user
    Parameters:
    :user - str with Twitter user nickname
    :number - maximum number of people to be checked
    Return:
    Dictionary -  where keys are Twitter nichnames of the followed people and
                        values are people location stated on Twitter
    """

    twitter_url = 'https://api.twitter.com/1.1/friends/list.json'
    url=twurl.augment(twitter_url, {'screen_name': user, 'count': number})
    data=urllib.request.urlopen(url).read().decode()
    users_json=json.loads(data)['users']
    following_people__location_dictioanary = {person["screen_name"]:person['location'] for person in users_json}
    return following_people__location_dictioanary
