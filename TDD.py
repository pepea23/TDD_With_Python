import unittest

# [lift1 ,lift2, lift3, lift4]
lifts = [2, 3, 3, 5]

class LiftTest(unittest.TestCase):
    def test_curent_floor_1_should_be_lift1(self):
        expexted = 2
        result = handleLift(1)
        self.assertEqual(result, expexted)
    
    def test_curent_floor_2_should_be_lift1(self):
        expexted = 2
        result = handleLift(2)
        self.assertEqual(result, expexted)

    def test_curent_floor_3_should_be_lift2(self):
        expexted = 3
        result = handleLift(3)
        self.assertEqual(result, expexted)


def handleLift(num):
        id =  min(range(len(lifts)), key=lambda i: abs(lifts[i]-num))
        return lifts[id]


unittest.main()