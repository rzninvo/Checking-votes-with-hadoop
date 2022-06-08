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
    created_at, tweet_id, tweet, likes, retweet_count, source, user_id, username, user_screen_name, user_description, user_join_date, user_followers_count, user_location, lat, long, city, country, continent, state, state_code, collected_at = cols
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

    result = f'{kind}{SEPARATOR}{state}'
    return result


for row in csv.reader(sys.stdin):
    try:
        result = mapper(row)
        if result is not None:
            print(result)
    except:
        pass