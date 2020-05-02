import json
import requests
import copy
from statistics import mean
with open('key.txt') as f:
    key = f.read()

with open('constants/big_items.json') as f:
    big_items = json.load(f)
    big_items = set(big_items.keys())

FILE = 'data/matches.txt'


def parse():
    data = read_match_list()
    purchase_dataset = {}
    for match in data:
        print(match)
        match_data = get_match_data(match)
        purchase_log = get_purchase_times(match_data)
        if purchase_log == {}:
            continue
        purchase_dataset = join_to_dataset(purchase_dataset,purchase_log)

    for item in purchase_dataset.keys():
        purchase_dataset[item] = mean(purchase_dataset[item])
    print('writing to disk')
    with open('data/purchase.json', 'w') as f:
        json.dump(purchase_dataset, f)

def join_to_dataset(purchase_dataset, purchase_log):
    for item in purchase_log.keys():
        if item not in purchase_dataset.keys():
            purchase_dataset[item] = purchase_log[item]
        else:
            purchase_dataset[item].extend(purchase_log[item])
    return purchase_dataset

def get_purchase_times(match):
    out = {}
    if 'players' not in match.keys():
        return {}
    for player in match['players']:
        if player['purchase_log'] == None:
            return {}
        for purchase in player['purchase_log']:
            if purchase['key'] not in out.keys():
                out[purchase['key']] = [purchase['time']]
            else:
                out[purchase['key']].append(purchase['time'])
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