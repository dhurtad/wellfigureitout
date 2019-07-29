
import urllib.request
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
    

    
    
