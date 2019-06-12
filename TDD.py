import unittest

lifts = [{'lift1':2},{'lift2':3},{'lift3':4}]

class LiftTest(unittest.TestCase):
    def test_curent_floor_1_should_be_lift1(self):
        expexted = 'lift1'
        result = handleLift(1)
        self.assertEqual(result,expexted)
    
def handleLift(num):
        return 'lift1'


unittest.main()