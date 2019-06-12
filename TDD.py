import unittest

lifts = [{1:2},{2:3},{3:4}]

class LiftTest(unittest.TestCase):
    def test_curent_floor_1_should_be_lift1(self):
        expexted = 1
        result = handleLift(1)
        self.assertEqual(result,expexted)
    



unittest.main()