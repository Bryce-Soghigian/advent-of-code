import typing
import os


def load_input():
    """
    Load fish timers.
    """
    with open(os.path.join(os.getcwd(), 'input.txt'), 'rt') as file:

        return [int(timer) for timer in file.read().split(",")]


class LanternFish:
    """
    Fish Object.
    """
    type = 'lantern_fish'

    def __init__(self, days_till_procreating: int = 8):
        self.timer: int = days_till_procreating


class LanternFishGrowthModel:
    """
    These fish keep spawning in my pool!

    I don't know a lot about these creatures but i do know one thing,
    I need to model their growth.

    We could just use dp but lets be real no one likes dp and thats no fun
    """

    def __init__(self, fish: typing.List['lantern_fish']):
        self.fish: typing.List['lantern_fish'] = []

        for timer in fish:
            self.fish.append(LanternFish(days_till_procreating=timer))

    def _add_k_fish(self, k: int):

        for _ in range(k):
            self.fish.append(LanternFish())

    def _emulate_day(self):
        """
        Each day we want to go through our queue, convert fish of zero into 6, and add a new 8 fish
        """
        fish_to_create: int = 0
        for lantern_fish in self.fish:
            lantern_fish.timer -= 1
            if lantern_fish.timer == -1:
                fish_to_create += 1
                lantern_fish.timer = 6

        self._add_k_fish(fish_to_create)

    def __call__(self, time: int):

        while time != 0:
            self._emulate_day()
            time -= 1

        return len(self.fish)


fish_timers = load_input()
calculate_growth_rate = LanternFishGrowthModel(fish_timers)
print(calculate_growth_rate(80))


def bottom_up(growth_rate: int):
    """
    Nevermind we need dp fuck.
    """

    population: typing.Dict[int] = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }

    for i in load_input():
        population[i] += 1
    for _ in range(growth_rate):
        population = {
            0: population[1], 1: population[2],
            2: population[3], 3: population[4],
            4: population[5], 5: population[6],
            6: population[0] + population[7],
            7: population[8],
            8: population[0]
        }

    result: int = 0
    for value in population.values():
        result += value
    return result


print(bottom_up(256))
