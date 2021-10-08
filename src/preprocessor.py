import numpy as np
from typing import List

def remove_long_music(list_music_time: List[int], work_time_minute:int) -> List[int]:
    target_index = np.where(np.array(list_music_time) <= work_time_minute * 60)[0]
    return [list_music_time[i] for i in target_index]

class InputPreprocessor():
    def __init__(self, work_time_minute: int):
        self.work_time_minute = work_time_minute

    def preprocess_input(self, list_music_time: List[int]) -> List[int]:
        list_music_time = remove_long_music(list_music_index, self.work_time_minute)
        return list_music_time

