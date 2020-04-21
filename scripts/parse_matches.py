import json

def parse():


def get_purchase_log(match):
    out = {}
    for x in match['players']:
        out[x['hero_id']] = x['purchase_log'] 
    return out


if __name__ =='__main__':
    parse()