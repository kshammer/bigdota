import requests
import time
import json

from urllib.parse import quote

with open('key.txt') as f:
    key = f.read()

def get_unix_time_yesterday():
    current_time = time.time()
    yesterday = current_time - 86400 # one day in unix time
    return int(yesterday)

def read_sql():
    with open('scripts/get_data.sql', 'r') as f:
        sql = f.read()
    yesterday = get_unix_time_yesterday()
    sql = sql.format(yesterday=str(yesterday))
    quoted_sql = quote(sql)
    return quoted_sql

def clean_data(obj):
    match_ids = []
    for match in obj['rows']:
        match_ids.append(match['match_id'])
    return match_ids

def get_data_sql():
    sql = read_sql()
    r = requests.get('https://api.opendota.com/api/explorer?sql={}&api_key={}'.format(sql, key))
    match_ids = clean_data(r.json())
    with open('data/matches.txt', 'w') as f:
        for match in match_ids:
            f.write(str(match))
            f.write('\n')

if __name__ == '__main__':
    get_data_sql()