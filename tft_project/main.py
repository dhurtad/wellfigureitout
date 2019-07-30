
import urllib.request
# import goody
# import prompt
from collections import defaultdict
import json

def get_tft_dict(url: str) -> dict:
    '''
    Downloads champion unit data from an api found online and
    returns a dictionary of champion units with their individual
    data. 
    '''
    response = urllib.request.urlopen(url)
    data = response.read()
    response.close()
    text = data.decode(encoding='utf-8')

    return json.loads(text)

def fix_unit_name(unit: str) -> str:
    '''
    Capitalizes the first letter in a string.
    '''
    unit = list(unit.lower())
    unit[0] = unit[0].upper()
    unit = ''.join(unit)
    return unit

def find_comp_origins_classes(comp: [str]) -> [str]:
    '''
    Returns two lists, one containing the origins and
    the other the classes of the comp.
    '''
    origin_list = []
    class_list = []
    for x in comp:
        unit = fix_unit_name(x)
        origins = get_tft_dict("https://solomid-resources.s3.amazonaws.com/blitz/tft/data/champions.json")[unit]['origin']
        classes = get_tft_dict("https://solomid-resources.s3.amazonaws.com/blitz/tft/data/champions.json")[unit]['class']

        for origin in origins:
            origin_list.append(origin)

        for blass in classes:
            class_list.append(blass)

    return origin_list, class_list

def count_dict(alist: [str]) -> {str : int}:
    '''
    Returns a defaultdict with the string as
    a key and the number of times the string is
    in the list the value.
    '''
    final_dict = defaultdict(int)
    for x in alist:
        final_dict[x] += 1

    return final_dict

def get_slots(data):
    """
    Returns a dictionary with the number
    of units required to receive a bonus
    in the form of a defaultdict.
    """
    class_dict = defaultdict(list)
    for x in data.keys():
        for bonus in data[x]['bonuses']:
            class_dict[x].append(bonus['needed'])
    return class_dict











    
    
