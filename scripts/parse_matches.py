import json
import requests
import copy
with open('key.txt') as f:
    key = f.read()

with open('constants/big_items.json') as f:
    big_items = json.load(f)
    big_items = set(big_items.keys())

FILE = 'data/matches.txt'


def parse():
    data = read_match_list()
    for match in data:
        match_data = get_match_data(match)
        purchase_log = get_purchase_log(match_data)
        cleaned_data = clean_data(purchase_log)
        with open('data/purchase.json', 'a') as f:
            json.dump(cleaned_data, f)
            f.write('\n')

def clean_data(purchase_log):
    purchase_data = copy.deepcopy(purchase_log)
    hero_keys = list(purchase_data.keys())
    hero_keys.remove('match_id')
    for hero in hero_keys:
       purchase_data[hero] = filter_big_items(purchase_data[hero])

    return purchase_data

def filter_big_items(item_list):
    expensive_items = []
    if item_list == None:
        return []
    for item in item_list:
        if item['key'] in big_items:
            expensive_items.append(item)
    return expensive_items

def get_purchase_log(match):
    out = {}
    out['match_id'] = match['match_id']
    for x in match['players']:
        out[x['hero_id']] = x['purchase_log'] 
    return out

def get_match_data(match_id):
    r = requests.get('https://api.opendota.com/api/matches/{}?api_key={}'.format(match_id, key))
    return r.json()

def read_match_list():
    with open(FILE, 'r') as f:
        text = f.read()
        data_list = text.split('\n')
    return data_list

if __name__ =='__main__':
    parse()