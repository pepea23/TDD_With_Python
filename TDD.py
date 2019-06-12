import unittest

# [lift1 ,lift2, lift3, lift4]
lifts = [2, 3, 3, 5]
lifts = [{'floor':2,'status':'up'}, {'floor':3,'status':'down'}, {'floor':3,'status':'none'}, {'floor':5,'status':'down'}]


class LiftTest(unittest.TestCase):
    def test_curent_floor_1_should_be_lift1(self):
        expexted = 2
        result = handleLift(1,'up')
        self.assertEqual(result, expexted)
    
    def test_curent_floor_2_should_be_lift1(self):
        expexted = 2
        result = handleLift(2,'up')
        self.assertEqual(result, expexted)

    def test_curent_floor_3_should_be_lift2(self):
        expexted = 3
        result = handleLift(3,'up')
        self.assertEqual(result, expexted)


def handleLift(num,btn):
        id =  min(range(len(lifts)), key=lambda i: abs(lifts[i].get('floor')-num))
        return lifts[id].get('floor')


unittest.main()