import json
import requests

FILE = 'data/old_matches.json'

def parse():
    data = read_match_list()
    for match in data:
        match_data = get_match_data(match['match_id'])
        purchase_log = get_match_data(match_data)
        with open('data/old_purchase.json', 'a') as f:
            json.dump(purchase_log, f)
            f.write(',\n')

def get_purchase_log(match):
    out = {}
    out['match_id'] = match['match_id']
    for x in match['players']:
        out[x['hero_id']] = x['purchase_log'] 
    return out

def get_match_data(match_id):
    r = requests.get('https://api.opendota.com/api/matches/{}'.format(match_id))
    return r.json()

def read_match_list():
    data_list = []
    with open(FILE, 'r') as f:
        for jsonObj in f:
            data = json.loads(jsonObj)
            data_list.append(data)
    return data_list

if __name__ =='__main__':
    parse()