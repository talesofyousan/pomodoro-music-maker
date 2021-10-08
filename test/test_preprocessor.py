import unittest
import numpy as np
from src.preprocessor import InputPreprocessor, remove_long_music

class TestRemoveLongMusic(unittest.TestCase):
    def test_remove_long_music(self):
        full_inputs = [
            [100,200,300,400,500],
            [100,200,300,400,500, 10000],
        ]
        ans_inputs = [
            [100,200,300,400,500],
            [100,200,300,400,500]
        ]
        work_time_minute = 25
        fixed_input = [remove_long_music(x, work_time_minute) for x in ans_inputs]
        self.assertListEqual(fixed_input, ans_inputs)

