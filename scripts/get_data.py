import requests
import time
import json
import random
with open('key.txt') as f:
    key = f.read()

FILE = 'data/matches.json'

def get_data(match_list=0):
    for i in range(10):
        while True:
            if match_list != 0:
                new_match = match_list.pop(0)
                new_data = hit_api(new_match)
            else:
                new_data = hit_api()
            if new_data != []:
                break
        write_to_disk(new_data, FILE)
        match_list = get_oldest_match(new_data)

def get_oldest_match(matches):
    match_ids = []
    for match in matches:
        match_ids.append(match['match_id'])
    random.shuffle(match_ids)
    return match_ids 

def write_to_disk(data, file):
    for info in data:
        with open(file, 'a') as f:
            json.dump(info, f)
            f.write('\n')

def hit_api(lowest_match=0):
    if lowest_match == 0:
        url = 'https://api.opendota.com/api/publicMatches?mmr_descending=4000&api_key={}'.format(key)
    else:
        url = 'https://api.opendota.com/api/publicMatches?mmr_descending=4000&less_than_match_id={}&api_key={}'.format(lowest_match, key)
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    get_data()
