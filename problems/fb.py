from typing import List
from collections import OrderedDict
import pprint

pretty = pprint.PrettyPrinter.pprint

test2 = 'ABA'
test1 = 'BBBAB'
RESULT = ''
start_length = None


def switch_letter(n, c):
    global RESULT, start_length
    if not start_length:
        start_length = n - 1
    n = n - 1
    if n > -1:
        RESULT += 'A' if c[start_length - n] == 'B' else 'B'


def get_wrong_answers(n: int, c: str) -> str:
    switch_letter(n, c)
    if n < 0:
        return RESULT
    return get_wrong_answers(n - 1, c)


def battle_ship_practice():
    sample_input = [
        OrderedDict({'R': 2, 'C': 3, 'G': [[0, 0, 1], [1, 0, 1]]}),
        OrderedDict({'R': 2, 'C': 3, 'G': [[0, 0, 0], [0, 0, 0]]}),
    ]
    R, C, G = list(sample_input[1].values())

    class BattleShip:
        g_size = 0
        contains_battleship_count = 0

        def __init__(self, r: int, c: int, g: List[List[int]]):
            self.r, self.c, self.g = r, c, g
            self.g_size = r * c

        def get_hit_probability(self) -> float:
            return self.__hit_probability_recursive(0)

        def __hit_probability_recursive(self, i: int):
            if i >= self.r: return
            self.contains_battleship_count += self.g[i].count(1)
            self.__hit_probability_recursive(i + 1)
            # round(self.contains_battleship_count / self.g_size, 5)
            return self.contains_battleship_count / self.g_size  # not rounding passed all test cases

    battleship = BattleShip(R, C, G)
    hit_probility = battleship.get_hit_probability()
    print(f'Hit probability is {hit_probility}')
    debug_point = 1


def cafeteria_practice():
    N = 10
    K = 1
    M = 2
    S = [2, 6]

    class Cafeteria:
        def __init__(self, n, k, m, s):
            self.n = n
            self.k = k
            self.m = m
            self.s = s

        def get_max_additional_diner_count(self) -> int:
            a = [n for n in range(1, 11)]
            tracker = [0 for _ in range(self.m)]
            for i in self.s:
                pos = self.s.index(i)
                bound = [x for x in range(self.k)]
                tracker[-self.k:pos] = 0
                tracker[self.k:pos] = 0
            return 0

    def get_max_addtional_diner_count(n: int, k: int, m: int, s: List[int]) -> int:
        caf = Cafeteria(n, k, m, s)
        return caf.get_max_additional_diner_count()

    get_max_addtional_diner_count(N, K, M, S)


cafeteria_practice()
# battle_ship_practice()
# get_wrong_answers(len(test1), test1)


#
