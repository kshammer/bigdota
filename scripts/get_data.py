import requests
import time
import json
import random
with open('key.txt') as f:
    key = f.read()

FILE = 'data/matches.json'
MATCH_SET = set()

# add another set of less than match ids to get a more varried set
def get_data(match_list=[]):
    for i in range(400):
        while True:
            if match_list != []:
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
        cleaned_data = clean_data(info)
        if cleaned_data != 0:
            with open(file, 'a') as f:
                json.dump(cleaned_data, f)
                f.write('\n')

def clean_data(match_info):
    if match_info['lobby_type'] != 7:
        return 0
    if match_info['avg_mmr'] == None:
        return 0
    if match_info['avg_mmr'] <= 4000:
        return 0
    if match_info['match_id'] in MATCH_SET:
        return 0
    MATCH_SET.add(match_info['match_id'])
    return match_info

def hit_api(lowest_match=0):
    if lowest_match == 0:
        url = 'https://api.opendota.com/api/publicMatches?mmr_descending=4000&api_key={}'.format(key)
    else:
        url = 'https://api.opendota.com/api/publicMatches?mmr_descending=4000&less_than_match_id={}&api_key={}'.format(lowest_match, key)
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    get_data()
