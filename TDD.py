import unittest

# [lift1 ,lift2, lift3, lift4]
lifts = [{'liftID': 1, 'floor': 2, 'status': 'up'}, {'liftID': 2, 'floor': 3, 'status': 'down'}, {'liftID': 3, 'floor': 3, 'status': 'none'}, {'liftID': 4, 'floor': 3, 'status': 'down'}]


class LiftTest(unittest.TestCase):
    def test_curent_floor_1_should_be_lift1(self):
        expexted = [3,'none']
        result = handleLift(1,'up')
        self.assertEqual(result, expexted)
    
    def test_curent_floor_2_should_be_lift1(self):
        expexted = [2,'down']
        result = handleLift(2,'down')
        self.assertEqual(result, expexted)

    def test_curent_floor_3_but_have_3_lift_same_floorshould_be_lift2(self):
        expexted = [3,'none']
        result = handleLift(3,'up')
        self.assertEqual(result, expexted)


def handleLift(num,btn):
        temps = []
        size = len(lifts)
        for i in range(size):
                if lifts[i].get('status') == btn or lifts[i].get('status') == 'none':
                    if lifts[i].get('status') == 'up' and lifts[i].get('floor') <= num:
                        temps.insert(i,lifts[i])
                    elif  lifts[i].get('status') == 'none' :
                        temps.insert(i,lifts[i])

                    if lifts[i].get('status') == 'down' and lifts[i].get('floor') >= num:
                        temps.insert(i,lifts[i])
                    elif  lifts[i].get('status') == 'none' :
                        temps.insert(i,lifts[i])
                        
        id =  min(range(len(temps)), key=lambda i: abs(temps[i].get('floor')-num))
        return [temps[id].get('liftID'),temps[id].get('status')]


unittest.main()