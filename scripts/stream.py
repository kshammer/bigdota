import requests
import time

with open('key.txt') as f:
    key = f.read()

def read_stream():
    while True:
        try:
            r = requests.get('https://api.opendota.com/api/feed?api_key={}&game_mode=7'.format(key), stream=True)
            for line in r.iter_lines():
                print(line)
                if line:
                    print('wrote a non-heartbeat')
                    with open('data/new_matches.json', 'a') as f:
                        f.write(str(line))
                        f.write(',\n')
        except:
            print('=)')
        finally:
            time.sleep(900)

if __name__ == '__main__':
    read_stream()