# Champ_Table object: Contains champ/origin/class 
# information to display to the player

import main

class Champ_Data:
    def __init__(self, origins: {str: int}, classes: {str: int}):
        ''' 
        Store origin and class data into a table-like object
        '''
        self.origins = []
        self.classes = []
        for origin in origins.keys():
            self.origins.append(origin.upper())     # Eliminate need to worry about uppercase/lowercase
        for blass in classes.keys():
            self.classes.append(blass.upper())
            
        self.champ_data_raw = main.get_tft_dict("https://solomid-resources.s3.amazonaws.com/blitz/tft/data/champions.json")
    
    def __repr__(self):
        return 'Champ_Data(' + str(self.origins) + ',' + str(self.classes) + ')'
    
    def get_all_origin_options(self):
        ''' 
        NOTE: Method might not be very efficient, as this 
        will provide the player with ALL possible future
        origins for the given current comp origins
        '''
        pass
    
    def get_all_class_options(self):
        '''
        NOTE: Method might not be very efficient, as this 
        will provide the player with ALL possible future 
        classes for the given current comp classes
        '''
        pass
    
    def get_origin_options(self, champ_origin: str):
        '''
        Player is prompted for a desired origin to build
        on, returns a list of possible champs based on 
        similar origin
        '''
        champ_list = []
        if champ_origin.upper() not in self.origins:            # Works since everything in self.origins is capitalized already
            raise NameError(f"'{champ_origin}' does not exist in comp.")
        for champ, data in self.champ_data_raw.items():
            if champ_origin in data['origin']:          # data['origin'] is a list
                champ_list.append(champ)
        return champ_list
    
    def get_class_options(self, champ_class: str):
        '''
        Player is prompted for a desired class to build
        on, returns a list of possible champs based on 
        similar class
        '''
        champ_list = []
        if champ_class.upper() not in self.classes:
            raise NameError(f"'{champ_class}' does not exist in comp.")
        for champ, data in self.champ_data_raw.items():
            if champ_class in data['class']:
                champ_list.append(champ)
        return champ_list
