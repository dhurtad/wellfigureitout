import unittest
import unit
import main

class TestingModule(unittest.TestCase):
    
    #Testing unit module
    def test_unit_name(self):
        test_champ = unit.champion('name', [1], 1, 1)
        test_champ.get_name() == 'name'

    def test_unit_origin(self):
        test_champ = unit.champion('name', [1], 1, 1)
        test_champ.get_origin() == 1

    def test_unit_class(self):
        test_champ = unit.champion('name', [1], 1, 1)
        test_champ.get_blass() ==[1]

    def test_unit_cost(self):
        test_champ = unit.champion('name', [1], 1, 1)
        test_champ.get_cost() == 1
        

if __name__ == '__main__':
    unittest.main()
