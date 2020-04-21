import requests
import time
with open('key.txt') as f:
    key = f.read()

def get_data():
    print('hello')
    for i in range(10):
        data = hit_api_old()
        for info in data:
            with open('data/old_matches.json', 'a') as f:
                f.write(str(info))
                f.write(',\n')
        time.sleep(600)
        print(i)


def hit_api_old():
    r = requests.get('https://api.opendota.com/api/publicMatches?mmr_descending=400&less_than_match_id=5362560977&api_key={}'.format(key))
    return r.json()

def get_data_new():
    print('hello')
    for i in range(10):
        data = hit_api_new()
        for info in data:
            with open('data/test_new.json', 'a') as f:
                f.write(str(info))
                f.write(',\n')
        time.sleep(300)
        print(i)

def hit_api_new():
    r = requests.get('https://api.opendota.com/api/publicMatches?mmr_descending=400&less_than_match_id=5369283534&api_key={}'.format(key))
    return r.json()

if __name__ == '__main__':
    get_data_new()
