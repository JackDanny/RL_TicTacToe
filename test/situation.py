import unittest
from main import similar_situation_90deg_clockwise, similar_situation_mirror, similar_situation_change_player

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_similar_situation_90deg_clockwise(self):
        situation = '0123456789'
        similar_situation = similar_situation_90deg_clockwise(situation)
        self.assertEqual(similar_situation, '0741852963')

    def test_similar_situation_90deg_clockwise_complete_turn(self):
        situation = '0123456789'
        similar_situation_90 = similar_situation_90deg_clockwise(situation)
        similar_situation_180 = similar_situation_90deg_clockwise(similar_situation_90)
        similar_situation_270 = similar_situation_90deg_clockwise(similar_situation_180)
        similar_situation_360 = similar_situation_90deg_clockwise(similar_situation_270)

        self.assertEqual(similar_situation_360, situation)

    def test_similar_situation_mirror(self):
        situation = '0123456789'

        similar_situation = similar_situation_mirror(situation)

        self.assertEqual(similar_situation, '0321654987')

        self.assertEqual(similar_situation_mirror(similar_situation), situation)

    def test_similar_similar_situation_change_player(self):
        situation = '2021211021'
        similar_situation = similar_situation_change_player(situation)
        self.assertEqual(similar_situation,'1012122012')

if __name__ == '__main__':
    unittest.main()
