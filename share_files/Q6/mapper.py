#!/usr/bin/env python
import datetime
import sys
import csv
from typing import Union

KIND_BIDEN = "Joe_Biden"
KIND_TRUMP = "Donald_Trump"
KIND_BOTH = "Both_Candidates"

biden_keywords = ["#Biden", "#JoeBiden"]
trump_keywords = ['#Trump', "#DonaldTrump"]
SEPARATOR = '|=|'


def mapper(cols: list) -> Union[str, None]:

    created_at, tweet_id, tweet, likes, retweet_count, source, user_id, username, user_screen_name, user_description, user_join_date, user_followers_count, user_location, lat, lon, city, country, continent, state, state_code, collected_at = cols
    tweet = tweet

    trump_condition = any([item in tweet for item in trump_keywords])
    biden_condition = any([item in tweet for item in biden_keywords])

    if trump_condition and biden_condition:
        kind = KIND_BOTH
    elif trump_condition:
        kind = KIND_TRUMP
    elif biden_condition:
        kind = KIND_BIDEN

    date = datetime.datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
    if date.hour < 9 or 17 <= date.hour:
        return None
    lat, lon = float(lat), float(lon)
    if -79.7624 < lon < -71.7517 and 40.4772 < lat < 45.0153:
        state_inferred_from_lat_and_long = 'New York'
    elif -124.6509 < lon < -114.1315 and 32.5121 < lat < 42.0126:
        state_inferred_from_lat_and_long = "Texas"
    else:
        return None
    result = f'{kind}{SEPARATOR}{state_inferred_from_lat_and_long}'
    return result


for row in csv.reader(sys.stdin):
    try:
        result = mapper(row)
        if result is not None:
            print(result)
    except:
        pass