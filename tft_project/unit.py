'''
ORIGIN LEGEND

1 DEMON
2 DRAGON
3 EXILE
4 GLACIAL
5 IMPERIAL
6 NINJA
7 NOBLE
8 PHANTOM
9 PIRATE
10 ROBOT
11 VOID
12 WILD
13 YORDLE


CLASS LEGEND

1 ASSASSIN
2 BLADEMASTER
3 BRAWLER
4 ELEMENTALIST
5 GUARDIAN
6 GUNSLINGER
7 KNIGHT
8 RANGER
9 SHAPESHIFTER
10 SORCERER

'''

class champion:

    def __init__(self, blasses: [int], origin: int, cost: int):
        self.blass = blasses
        self.origin = origin
        self.cost = cost

    def get_origin(self):
        return self.origin

    def get_blass(self):
        return self.blass

    def get_cost(self):
        return self.cost
        
    
