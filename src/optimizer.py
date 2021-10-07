import pulp as pp
import numpy as np
from collections import Counter
import itertools
from pydantic import BaseModel
from typing import List

class SampleData(BaseModel):
    list_music_time : List[int] = [257, 229, 266, 226, 278, 220, 273, 271, 206, 284, 187, 194, 201, 186, 278, 274, 195, 288, 181, 230]  

class Recommender():
    def __init__(self):
        self.work_time_minute: int = 25
        self.break_time_minute: int = 5
        self.random_selection_ratio: float = 0.5

    def get_optimized_result(self, list_music_time, is_random=True):
        if is_random:
            idx_music_time = list(range(len(list_music_time)))
            np.random.shuffle(idx_music_time)
            R = 0
            random_selected_index = []
            for idx in idx_music_time:
                R += list_music_time[idx]
                random_selected_index.append(idx)
                if self.work_time_minute * 60 * self.random_selection_ratio <= R:
                    break
        else:
            R = 0
            random_selected_index = []

        candidate_index = [i for i in range(len(list_music_time)) if not i in random_selected_index]
        problem = pp.LpProblem('MusicSchedule', pp.LpMinimize)
        vec_x = pp.LpVariable.dicts('selected', (set(candidate_index)), 0, 1, 'Integer')

        # Variable to hold sum
        sum_var = pp.LpVariable('sum_var')
        abs_sum_var = pp.LpVariable('abs_sum_var')

        # Objective
        problem += abs_sum_var
        # subject to
        problem += sum_var == pp.lpSum([list_music_time[idx] * vec_x[idx] for idx in candidate_index] + [R , -25 * 60])
        problem += abs_sum_var >= sum_var
        problem += abs_sum_var >= -sum_var
        problem += pp.lpSum([vec_x[idx] for idx in candidate_index]) >= 1

        problem.solve()
        selected_index = []
        for v in problem.variables():
            if v.varValue == 1 and 'selected' in v.name:
                selected_index.append(int(v.name.split('_')[-1]))

        return random_selected_index + selected_index

    def get_recommended_music_index(self, list_music_time):
        num_cycle = int(sum(list_music_time) / (self.work_time_minute*60))
        list_music_index = list(range(len(list_music_time)))

        list_selected_index = []
        tmp_list_music_time = list_music_time
        tmp_list_music_index = list_music_index
        for i in range(num_cycle):
            if i == 0:
                tmp = self.get_optimized_result(tmp_list_music_time)
            else:
                tmp = self.get_optimized_result(tmp_list_music_time, is_random=False)
            list_selected_index.append([tmp_list_music_index[i] for i in tmp])
            tmp_list_music_time = [t for i, t in enumerate(tmp_list_music_time) if not i in tmp]
            tmp_list_music_index = [idx for i, idx in enumerate(tmp_list_music_index) if not i in tmp]

        return list_selected_index