
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






    
    
