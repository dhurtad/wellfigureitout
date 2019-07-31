# Runs main event loop

import main
import prompt
from champ_data import Champ_Data

if __name__ == '__main__':
    # Execute necessary functions here
    game_status = True
    champs = main.get_tft_dict(main.CHAMP_API)
    # print(champs)
    class_slots = main.get_slots(main.get_tft_dict(main.CLASSES_API))
    origin_slots = main.get_slots(main.get_tft_dict(main.ORIGINS_API))
    print(class_slots)
    print(origin_slots)
    
    while game_status:
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

        origins, classes = main.find_comp_origins_classes(comp)
        origins = main.count_dict(origins)
        classes = main.count_dict(classes)
        
        print('Your current origins are: ')
        print(dict(origins))
        print('Your current classes are: ')
        print(dict(classes))
        
        # Returning relevant information/data to player
        
        champ_data = Champ_Data(dict(origins), dict(classes))
        choice = prompt.for_int('Would you like to build your comp off of an origin (0) or class (1)')
        while True:
            try:
                if choice == 0:
                    origin = prompt.for_string('Which origin would you like to build off of? Please input an origin')
                    print('Your origin options are: ', champ_data.get_origin_options(origin))
                    break
                else:
                    blass = prompt.for_string('Which origin would you like to build off of? Please input an origin')
                    print('Your class options are: ', champ_data.get_class_options(blass))
                    break
            except NameError:
                print('Invalid origin/class')
            
        
        # Ask if game has ended or not (Only for console version; this is temporary)
        game_status_input = prompt.for_string('Has the game ended? (Y or N)')
        if game_status_input.upper() == 'Y':
            print('Goodbye!')
            game_status = False
        
