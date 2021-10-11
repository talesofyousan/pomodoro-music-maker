import unittest
import numpy as np
from src.recommender import Recommender

class TestRecommendedMusicIndex(unittest.TestCase):
    def test_basic(self):
        sample_input = [100, 110, 120, 130, 140, 160, 170, 180, 190, 200, 101]
        recommendation = Recommender(25, 5, 0.5, 10, 123).get_recommended_music_index(sample_input)
        sum_val = sum([sample_input[i] for i in recommendation[0]])
        self.assertTupleEqual(np.shape(recommendation), (1, 10))
        self.assertEqual(sum_val, 25*60)
