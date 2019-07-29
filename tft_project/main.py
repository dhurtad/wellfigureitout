
import urllib.request
import goody
import prompt
import json


def get_champ_dict() -> dict:
    '''
    Downloads champion unit data from an api found online and
    returns a dictionary of champion units with their individual
    data. 
    '''
    url = "https://solomid-resources.s3.amazonaws.com/blitz/tft/data/champions.json"
    response = urllib.request.urlopen(url)
    data = response.read()
    response.close()
    text = data.decode(encoding = 'utf-8')

    return json.loads(text)

def fix_unit_name(unit: str) -> str:
    unit = list(unit.lower())
    unit[0] = unit[0].upper()
    unit = ''.join(unit)
    return unit

def find_comp_origins_classes(comp: [str]) -> [str]:
    origin_list = []
    class_list = []
    for x in comp:
        unit = fix_unit_name(x)
        origins = get_champ_dict()[unit]['origin']
        classes = get_champ_dict()[unit]['class']

        for origin in origins:
            origin_list.append(origin)

        for blass in classes:
            class_list.append(blass)

    return origin_list, class_list


if __name__ == '__main__':
    champs = get_champ_dict()
    while True:
        level = prompt.for_int('Input your current level')
        comp = []

        for x in range(level):
            while True:
                champ = prompt.for_string('Input champ #' + str(x+1))
                if champ.upper() in [x.upper() for x in champs.keys()]:
                    comp.append(champ)
                    break

                else:
                    print('This is not a valid unit name')

        origins, classes = find_comp_origins_classes(comp)
        print(origins, classes)









    
    
