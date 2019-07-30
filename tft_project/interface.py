# Runs main event loop

import main
import prompt

if __name__ == '__main__':
    # Execute necessary functions here
    game_status = True
    champs = main.get_tft_dict(main.CHAMP_API)
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
        
        print(origins)
        print(classes)
        
        # Ask if game has ended or not (Only for console version; this is temporary)
        game_status_input = prompt.for_string('Has the game ended? (Y or N)')
        if game_status_input.upper() == 'Y':
            print('Goodbye!')
            game_status = False
        
